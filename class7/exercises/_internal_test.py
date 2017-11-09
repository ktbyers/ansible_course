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
EXERCISES = [
###    ('/home/kbyers/ansible_course/class7/exercises/exercise1.yml', 
###        {'tests': 
###            {
###                'return_code': 0,
###                'return_strings': [
###                    'nxos1                      : ok=4',
###                    'nxos2                      : ok=4',
###                    'pynet-rtr1                 : ok=4',
###                    'pynet-rtr2                 : ok=4',
###                    'pynet-sw5                  : ok=4',
###                    'pynet-sw6                  : ok=4',
###                    'pynet-sw7                  : ok=4',
###                    'pynet-sw8                  : ok=4',
###                    'TASK [Generate global configuration]',
###                    'PLAY [Generate Global Configuration Items (Part1)]',
###                    'PLAY [Deploy configuration using Ansible Core (IOS): Part1b]',
###                    'TASK [ios_config]',
###                    'PLAY [Deploy configuration using Ansible Core (NX-OS): Part1b]',
###                    'TASK [nxos_config]',
###                    'PLAY [Deploy configuration using Ansible Core (Arista): Part1b]',
###                    'TASK [eos_config]',
###                ]
###            }
###        }),
###    ('/home/kbyers/ansible_course/class7/exercises/exercise2.yml', 
###        {'tests': 
###            {
###                'return_code': 0,
###                'return_strings': [
###                    'nxos1                      : ok=3',
###                    'nxos2                      : ok=3',
###                    'PLAY [Generate and Deploy BGP Configurations]', 
###                    'TASK [Gathering Facts]',
###                    'TASK [Generate BGP Configs (part2)]', 
###                    'TASK [Push Configs using NAPALM: Merge (part2b)]',
###                ]
###            }
###        }),
    ('/home/kbyers/ansible_course/class7/exercises/exercise3.yml', 
        {'tests': 
            {
                'return_code': 0,
                'return_strings': [
                    'nxos1                      : ok=2',
                    'nxos2                      : ok=2',
                    'PLAY [Generate NX-OS Configuration Files]',
                    'TASK [Generate NX-OS Configuration Files]',
                ]
            }
        }),
    ('/home/kbyers/ansible_course/class7/exercises/exercise3b.yml', 
        {'tests': 
            {
                'return_code': 0,
                'return_strings': [
                    'nxos1                      : ok=2',
                    'nxos2                      : ok=2',
                    'PLAY [Generate NX-OS Configuration Files Macro]',
                    'TASK [Generate NX-OS Configuration Files Macro]',
                ]
            }
        }),
    ('/home/kbyers/ansible_course/class7/exercises/exercise3c.yml', 
        {'tests': 
            {
                'return_code': 0,
                'return_strings': [
                    'nxos1                      : ok=2',
                    'nxos2                      : ok=2',
                    'PLAY [Generate BGP + VRF Configurations]',
                    'TASK [Generate BGP + VRF Configs]',
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
    print("Testing Ansible Network Automation Class")
    for ansible in [ACTIVE_VERSION,]:
        ansible_version = get_ansible_version(ansible)
        print("Testing Ansible Version: {}".format(ansible_version))

        for test_script, test_attr in EXERCISES:
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
