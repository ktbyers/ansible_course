## Obscure SSH Messages from Ansible Core Networking Modules

### Ansible 2.3 and 2.4

fatal: [pynet-rtr1]: FAILED! => {"changed": false, "failed": true, "msg": "unable to open shell. Please see: https://docs.ansible.com/ansible/network_debug_troubleshooting.html#unable-to-open-shell", "rc": 255}

### The above URL points us here:

http://docs.ansible.com/ansible/latest/network_debug_troubleshooting.html#enable-network-logging

### This URL tells us to do this:

    export ANSIBLE_DEBUG=True
    export ANSIBLE_LOG_PATH=~/ansible.log

    And run playbook with '-vvvv'


### In the ~/ansible.log file search for the IP address or DNS name

    p=19840 u=kbyers |  connecting to host cisco1.domain.com returned an error
    p=19840 u=kbyers |  (14, 'Bad address')
    
'Bad address' = Entry not found in SSH known_hosts (there could be other causes for this message)

    paramiko.transport Authentication (password) failed.
    p=27514 u=kbyers |  connecting to host cisco1.domain.com returned an error
    p=27514 u=kbyers |  Authentication failed.

'Authentication Failed' will occur when your password is not valid and there should be a 'paramiko' password failed message close to this in the log.
