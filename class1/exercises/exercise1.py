#!/usr/bin/env python
"""
Create a YAML list in a file.

Use Python to read it and print it to the screen. The list should have at least four elements.
"""
from __future__ import print_function
import yaml
from pprint import pprint


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":

    filename = "exercise1.yml"
    pprint(read_yaml(filename))
