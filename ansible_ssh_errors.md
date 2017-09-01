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

    p=27700 u=kbyers |  connecting to host cisco10.domain.com returned an error
    p=27700 u=kbyers |  [Errno -2] Name or service not known

'Name or service not known' this will occur when your specified hostname is not in DNS.

    p=18487 u=kbyers |  connecting to host cisco1.domain.com returned an error
    p=18487 u=kbyers |  No authentication methods available
    
'No authentication methods available' will occur if you do not have a password specified in your provider (and don't provide a password from the command line.

    p=27885 u=kbyers |  connecting to host 10.10.10.10 returned an error
    p=27885 u=kbyers |  timed out
    
'connecting to host <ip_address> returned an error' occurs when you specify an IP address that is not listening on SSH.
