#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals

from scripttest import TestFileEnvironment
import subprocess

env = TestFileEnvironment('./_test')
debug = False

# DEFINE ANSIBLE VERSION
ANSIBLE_2_3 = "/home/kbyers/VENV/py27_venv/bin/ansible-playbook"
ANSIBLE_2_4 = "/home/kbyers/VENV/ans_2_4/bin/ansible-playbook"
ACTIVE_VERSION = ANSIBLE_2_3

# DEFINE TEST CASES
PROGRAMS = [
    ('/home/kbyers/ansible_course/class3/exercises/exercise1.yml', 
        {'tests': 
            {
                'return_code': 0,
                'return_strings': [
                    'nxos1                      : ok=2    changed=1    unreachable=0    failed=0',
                    'nxos2                      : ok=2    changed=1    unreachable=0    failed=0',
                    "changed: [nxos1] => (item={u'name': u'blue', u'vlan_id': 301})",
                    "changed: [nxos2] => (item={u'name': u'blue', u'vlan_id': 301})",
                    "changed: [nxos1] => (item={u'name': u'red', u'vlan_id': 302})",
                    "changed: [nxos2] => (item={u'name': u'red', u'vlan_id': 302})",
                    "changed: [nxos1] => (item={u'name': u'green', u'vlan_id': 303})",
                    "changed: [nxos2] => (item={u'name': u'green', u'vlan_id': 303})",
                    "changed: [nxos1] => (item={u'name': u'yellow', u'vlan_id': 304})",
                    "changed: [nxos2] => (item={u'name': u'orange', u'vlan_id': 305})",
                    "changed: [nxos2] => (item={u'name': u'gray', u'vlan_id': 306})",
                ]
            }
        }),

    ('/home/kbyers/ansible_course/class3/exercises/exercise2.yml', 
        {'tests': 
            {
                'return_code': 0,
                'return_strings': [
                    "nxos1                      : ok=3    changed=2    unreachable=0    failed=0",
                    "nxos2                      : ok=3    changed=2    unreachable=0    failed=0",
                    'TASK [Configure IPv4 and IPv6 interfaces]',
                    "changed: [nxos2] => (item={u'type': u'v4', u'mask': 24, u'addr': u'10.1.1.2', u'name': u'Ethernet 2/4', u'remote_addr': u'10.1.1.1'})",
                    "changed: [nxos1] => (item={u'type': u'v4', u'mask': 24, u'addr': u'10.1.1.1', u'name': u'Ethernet 2/4', u'remote_addr': u'10.1.1.2'})",
                    "changed: [nxos2] => (item={u'type': u'v6', u'mask': 64, u'addr': u'2001:db8:800:200c::2', u'name': u'Ethernet 2/4', u'remote_addr': u'2001:db8:800:200c::1'})",
                    "changed: [nxos1] => (item={u'type': u'v6', u'mask': 64, u'addr': u'2001:db8:800:200c::1', u'name': u'Ethernet 2/4', u'remote_addr': u'2001:db8:800:200c::2'})",
                    "RUNNING HANDLER [write mem]",
                ]
            }
        }),

    ('/home/kbyers/ansible_course/class3/exercises/exercise3.yml', 
        {'tests': 
            {
                'return_code': 0,
                'return_strings': [
                    "nxos1                      : ok=2    changed=0    unreachable=0    failed=0",
                    "nxos2                      : ok=2    changed=0    unreachable=0    failed=0",
                    "PLAY [Exercise3]",
                    "TASK [Ping remote device]",
                    "skipping: [nxos2] => (item={u'type': u'v6', u'mask': 64, u'addr': u'2001:db8:800:200c::2', u'name': u'Ethernet 2/4', u'remote_addr': u'2001:db8:800:200c::1'})",
                    "ok: [nxos2] => (item={u'type': u'v4', u'mask': 24, u'addr': u'10.1.1.2', u'name': u'Ethernet 2/4', u'remote_addr': u'10.1.1.1'})",
                    "skipping: [nxos1] => (item={u'type': u'v6', u'mask': 64, u'addr': u'2001:db8:800:200c::1', u'name': u'Ethernet 2/4', u'remote_addr': u'2001:db8:800:200c::2'})",
                    "ok: [nxos1] => (item={u'type': u'v4', u'mask': 24, u'addr': u'10.1.1.1', u'name': u'Ethernet 2/4', u'remote_addr': u'10.1.1.2'})",
                ]
            }
        }),

    ('/home/kbyers/ansible_course/class3/exercises/exercise4.yml', 
        {'tests': 
            {
                'return_code': 0,
                'return_strings': [
                    "nxos1                      : ok=4    changed=3    unreachable=0    failed=0",
                    "nxos2                      : ok=4    changed=3    unreachable=0    failed=0",
                    "PLAY [Exercise4]",
                    "TASK [Configure SNMP Location]",
                    "TASK [Configure SNMP Contact]",
                    "RUNNING HANDLER [write mem]",
                ]
            }
        }),
]


def get_ansible_version(ansible):
    cmd_list = [ansible, '--version']
    proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (std_out, std_err) = proc.communicate()
    std_out = std_out.strip()
    return std_out.splitlines()[0]


def main():
    print("\n")
    print("-" * 80)
    print("Testing Ansible Network Automation: Class2")
    for ansible in [ACTIVE_VERSION,]:
        ansible_version = get_ansible_version(ansible)
        print("Testing Ansible Version: {}".format(ansible_version))

        for test_script, test_attr in PROGRAMS:
            cmd_args = test_attr.get('addl_args', ())
            print("TEST: {} {} ... ".format(test_script, cmd_args), end='')
            res = env.run(ansible, test_script, *cmd_args)
            tests = test_attr.get('tests')
            if tests.get('return_code') is not None:
                assert res.returncode == tests['return_code']
            return_strings = tests.get('return_strings', [])
            for test_string in return_strings:
                if debug:
                    print(test_string)
                assert test_string in res.stdout
            print("OK")

    print("Tests completed successfully")
    print("-" * 80)
    print("\n")

if __name__ == "__main__":
    main()
