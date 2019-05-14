#!/usr/bin/env python
"""
Create a YAML dictionary in a file. Use Python to read it and print it to the screen. The
dictionary should have at least four keys; one of the values in the dictionary should be a list.
"""
from __future__ import print_function
import yaml
from pprint import pprint


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":

    filename = "exercise2.yml"
    pprint(read_yaml(filename))
