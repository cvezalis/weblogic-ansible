db_server_name = '{{ dbserver_name }}'
db_server_port = '{{ dbserver_port }}'
db_service = '{{ dbserver_service }}'
data_source_url='jdbc:oracle:thin:@//' + db_server_name + ':' + db_server_port + '/' + db_service;
data_source_user_prefix= '{{ repository_prefix }}'
data_source_test='SQL SELECT 1 FROM DUAL';

domain_application_home = '{{ applications_home }}/{{ domain_name }}'
domain_configuration_home = '{{ domains_home }}/{{ domain_name }}'
domain_name = '{{ domain_name }}'
java_home = '{{ jdk_folder }}'
middleware_home = '{{ middleware_home }}'
node_manager_home = '{{ nodemanager_home }}'
weblogic_home = '{{ weblogic_home }}'

weblogic_template=weblogic_home + '/common/templates/wls/wls.jar';
em_template=middleware_home + '/em/common/templates/wls/oracle.em_wls_template_12.1.3.jar';

readTemplate(weblogic_template);
setOption('DomainName', domain_name);
setOption('OverwriteDomain', 'true');
setOption('JavaHome', java_home);
setOption('ServerStartMode', 'prod');
setOption('NodeManagerType', 'CustomLocationNodeManager');
setOption('NodeManagerHome', node_manager_home);
cd('/Security/base_domain/User/weblogic');
cmo.setName('{{ weblogic_admin }}');
cmo.setUserPassword('{{ weblogic_admin_pass }}');
cd('/');

print "SAVE DOMAIN";
writeDomain(domain_configuration_home);
closeTemplate();

print 'READ DOMAIN';
readDomain(domain_configuration_home);

print 'ADD TEMPLATES';
addTemplate(em_template);
#addTemplate(jrf_template);
#addTemplate(coherence_template);
setOption('AppDir', domain_application_home);

jdbcsystemresources = cmo.getJDBCSystemResources();
for jdbcsystemresource in jdbcsystemresources:
    cd ('/JDBCSystemResource/' + jdbcsystemresource.getName() + '/JdbcResource/' + jdbcsystemresource.getName() + '/JDBCConnectionPoolParams/NO_NAME_0');
    cmo.setInitialCapacity(1);
    cmo.setMaxCapacity(15);
    cmo.setMinCapacity(1);
    cmo.setStatementCacheSize(0);
    cmo.setTestConnectionsOnReserve(java.lang.Boolean('false'));
    cmo.setTestTableName(data_source_test);
    cmo.setConnectionCreationRetryFrequencySeconds(30);
    cd ('/JDBCSystemResource/' + jdbcsystemresource.getName() + '/JdbcResource/' + jdbcsystemresource.getName() + '/JDBCDriverParams/NO_NAME_0');
    cmo.setUrl(data_source_url);
    cmo.setPasswordEncrypted('{{ datasource_password }}');
   
    cd ('/JDBCSystemResource/' + jdbcsystemresource.getName() + '/JdbcResource/' + jdbcsystemresource.getName() + '/JDBCDriverParams/NO_NAME_0/Properties/NO_NAME_0/Property/user');
    cmo.setValue(cmo.getValue().replace('DEV',data_source_user_prefix));
    cd('/');

cd("/SecurityConfiguration/" + domain_name);
cmo.setNodeManagerUsername('{{ nodemanager_username }}');
cmo.setNodeManagerPasswordEncrypted('{{ nodemanager_password }}');

cd('/Server/' + '{{ admin_server_name }}');
create('{{ admin_server_name }}','SSL');
cd('SSL/' + '{{ admin_server_name }}');
cmo.setHostnameVerificationIgnored(true);
cmo.setHostnameVerifier(None);
cmo.setTwoWaySSLEnabled(false);
cmo.setClientCertificateEnforced(false);

cd('/SecurityConfiguration/'+ domain_name +'/Realms/myrealm');
cd('AuthenticationProviders/DefaultAuthenticator');
set('ControlFlag', 'SUFFICIENT');
cd('../../');

updateDomain();
closeDomain();
