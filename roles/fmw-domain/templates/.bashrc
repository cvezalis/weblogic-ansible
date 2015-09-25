if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

export DOMAINS_HOME={{ domains_home }}
export APPLICATIONS_HOME={{ applications_home }}
