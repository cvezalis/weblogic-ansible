nmConnect('{{ nodemanager_username }}', '{{ nodemanager_password }}', '{{ node_manager_listen_address }}', '{{ node_manager_listen_port }}', '{{ domain_name }}');

nmStart('{{ admin_server_name }}');

nmDisconnect();
