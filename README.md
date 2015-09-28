# weblogic-ansible
An Ansible Playbook (weblogic-fmw-domain.yml) for install and configure a WebLogic server 12c with 
Oracle Fussion Middleware Software for hosting Oracle Fussion Middleware (for example ADF applications) in Redhat Linux 7 (RHEL/CentOS/Oracle Linux) system.
This playbook is for version 12.1.3 of WebLogic and Fussion Middleware Infrastructure software.

Requirements for running the playbook:
- Configure your environment variables in infra-vars.yml. 
- Set your passwords in secrets.yml.
- A running Oracle Database for hosting the repositories is required and sys user password for generates the repositories.
- A running RHEL 7 system with minimal installation with network configured. (IP address, hostname etc)

The playbook includes the following Ansible Roles:
- linux-wls: Configures the linux system with required packages, kernel settings etc.
- linux-jdk: Installs Oracle JDK 7
- fmw-software: Installs Oracle Fussion Middleware Infrastructure software
- fmw-domain: Creates a Domain with Fussino Middleware support (Enterprise Manager, JRF, etc)
- fmw-managed-server: Creates a managed server for host applications

For test the playbook you can Download Vagrant and then run: 
- $ vagrant plugin install vagrant-hostmanager
- $ vagrant up
- $ ansible-playbook weblogic-fmw-domain.yml

When the playbook finishes execution you can connect to weblogic server using wls12c1.private:7001/console.