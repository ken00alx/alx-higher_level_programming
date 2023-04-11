#!usr/bin/python3
"""Module function lookup that returns list
of available object method and attribute
"""


def lookup(obj):
    """Returns the list of available attributes and
    methods of an object"""
    return (list(dir(obj)))
