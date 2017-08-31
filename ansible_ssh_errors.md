## Obscure SSH Messages from Ansible Core Networking Modules

### Ansible 2.3 and 2.4

fatal: [pynet-rtr1]: FAILED! => {"changed": false, "failed": true, "msg": "unable to open shell. Please see: https://docs.ansible.com/ansible/network_debug_troubleshooting.html#unable-to-open-shell", "rc": 255}

### The above URL points us here:

http://docs.ansible.com/ansible/latest/network_debug_troubleshooting.html#enable-network-logging

### This URL tells us to do this:

    export ANSIBLE_DEBUG=True
    export ANSIBLE_LOG_PATH=~/ansible.log

    And run playbook with '-vvvv'
