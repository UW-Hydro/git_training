#!/usr/bin/env python
"""
letters.py

A group of personal hello_world functions
"""

from __future__ import print_function
from datetime import date


def hello_world():
    print("Hello world!  Today's date is: {0}".format(date.today()))


def goodbye_world():
    print("Goodbye world!")


def hello_name(my_str):
    print("Hello SE-YEUN:  {0}".format(my_str))
