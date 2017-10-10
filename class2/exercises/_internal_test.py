#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals

from scripttest import TestFileEnvironment
import subprocess

env = TestFileEnvironment('./_test')
debug = False

# DEFINE ANSIBLE VERSION
ANSIBLE_2_3 = "/home/kbyers/VENV/py27_venv/bin/ansible-playbook"
#ANSIBLE_2_4 = "/home/kbyers/VENV/ans_2_4/bin/ansible-playbook"

# DEFINE TEST CASES
CLASS2_PROGRAMS = [
    ('/home/kbyers/ansible_course/class2/exercises/exercise1.yml', 
        {'tests': 
            {
                'return_code': 0,
                'return_strings': [
                    'FTX1512038X',
                    'FTX18298312',
                    'pynet-rtr1                 : ok=2    changed=0    unreachable=0    failed=0',
                    'pynet-rtr2                 : ok=2    changed=0    unreachable=0    failed=0',
                ]
            }
        }),

    ('/home/kbyers/ansible_course/class2/exercises/exercise2.yml', 
        {'addl_args': ("--tags", "2a"),
         'tests':
            {
                'return_code': 0,
                'return_strings': [
                    'ansible_net_all_ipv4_addresses',
                    '10.220.88.21',
                    'pynet-rtr1                 : ok=1    changed=0    unreachable=0    failed=0',
                    'pynet-rtr2                 : ok=2    changed=0    unreachable=0    failed=0',
                ] 
            }
        }),

    ('/home/kbyers/ansible_course/class2/exercises/exercise2.yml', 
        {'addl_args': ("--tags", "2b"),
         'tests':
            {
                'return_code': 0,
                'return_strings': [
                    'pynet-rtr1                 : ok=2    changed=0    unreachable=0    failed=0',
                    'pynet-rtr2                 : ok=2    changed=0    unreachable=0    failed=0',
                    'FastEthernet0',
                    'FastEthernet1',
                    'FastEthernet2',
                    'FastEthernet3',
                    'FastEthernet4',
                    'Vlan1',
                ]
            }
        }),

    ('/home/kbyers/ansible_course/class2/exercises/exercise2.yml', 
        {'addl_args': ("--tags", "2c"),
         'tests':
            {
                'return_code': 0,
                'return_strings': [
                    'Active Interface: FastEthernet4',
                    'pynet-rtr1                 : ok=2    changed=0    unreachable=0    failed=0',
                    'pynet-rtr2                 : ok=2    changed=0    unreachable=0    failed=0',
                ]
            }
        }),

    ('/home/kbyers/ansible_course/class2/exercises/exercise2.yml', 
        {'addl_args': ("--tags", "2d"),
         'tests':
            {
                'return_code': 0,
                'return_strings': [
                    'pynet-rtr1                 : ok=2    changed=0    unreachable=0    failed=0',
                    'pynet-rtr2                 : ok=2    changed=0    unreachable=0    failed=0',
                    'ansible_net_model',
                    '881 (MPC8300) processor'
                ]
            }
        }),

]

PROGRAMS = CLASS2_PROGRAMS


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
    for ansible in [ANSIBLE_2_3,]:
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
