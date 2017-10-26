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
    ('/home/kbyers/ansible_course/class5/exercises/exercise1.yml', 
        {'tests': 
            {
                'return_code': 0,
                'return_strings': [
                    'pynet-rtr1                 : ok=7    changed=0    unreachable=0    failed=0', 
                    'pynet-rtr2                 : ok=7    changed=0    unreachable=0    failed=0',
                    'PLAY [NAPALM LLDP Verification]',
                    'TASK [Bonus where not hard-coding name (with_items will retrieve the key)]',
                    '"lldp_info": {',
                    '"hostname": "twb-sf-hpsw1",', 
                    '"lldp_info_alt": {',
                    '"msg": "All assertions passed"',
                ]
            }
        }),
    ('/home/kbyers/ansible_course/class5/exercises/exercise2.yml', 
        {'tests': 
            {
                'return_code': 0,
                'return_strings': [
                    'nxos1                      : ok=6    changed=1    unreachable=0    failed=0',
                    'nxos2                      : ok=6    changed=1    unreachable=0    failed=0',
                    'PLAY [NAPALM Configure IP interface + Verify]',
                    'TASK [Configure IP interface (not idempotent)]',
                    'TASK [Verify IP interface]',
                    'ok: [nxos1] => (item=10.100.17.1)',
                    'ok: [nxos2] => (item=10.100.17.2)',
                    '"msg": "All assertions passed"',
                ]
            }
        }),
    ('/home/kbyers/ansible_course/class5/exercises/exercise3.yml', 
        {'tests': 
            {
                'return_code': 0,
                'return_strings': [
                    'nxos1                      : ok=7    changed=1    unreachable=0    failed=0',
                    'nxos2                      : ok=6    changed=1    unreachable=0    failed=0',
                    'PLAY [NAPALM configure BGP on NX-OS switches]',
                    'TASK [Configure BGP]',
                    'TASK [Give BGP time to come up (delay 10s)]',
                    'TASK [Verify BGP]',
                    '"10.100.17.2": {',
                    '"address_family": {',
                    '"local_as": 22,',
                    '"remote_as": 22,', 
                    '"remote_id": "10.100.17.2",', 
                    'ok: [nxos1] => (item=10.100.17.2) => {',
                    '"msg": "All assertions passed"',
                ]
            }
        }),
    ('/home/kbyers/ansible_course/class5/exercises/exercise4.yml', 
        {'tests': 
            {
                'return_code': 0,
                'return_strings': [
                    'pynet-sw8                  : ok=3    changed=1    unreachable=0    failed=0',
                    'PLAY [Full config load SW8 (diff only)]',
                    'TASK [Baseline config]',
                    'TASK [Print output when diff is not null string]',
                    'TASK [Load loopback interface config]',
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
    print("Testing Ansible Network Automation: Class5")
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
                    print('*' * 80)
                    print(res.stdout)
                assert test_string in res.stdout
            print("OK")

    print("Tests completed successfully")
    print("-" * 80)
    print("\n")

if __name__ == "__main__":
    main()
