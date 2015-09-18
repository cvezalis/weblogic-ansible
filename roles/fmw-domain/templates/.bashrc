if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

export JAVA_HOME={{ jdk_folder }}
export PATH=$PATH:$JAVA_HOME/bin

export ORACLE_HOME={{ middleware_home }}
export DOMAINS_HOME={{ domains_home }}
export APPLICATIONS_HOME={{ applications_home }}
