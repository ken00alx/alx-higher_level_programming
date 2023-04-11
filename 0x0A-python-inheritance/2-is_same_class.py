#!/usr/bin/python3
"""A method with name is_name_class, which returns
True if the object is exactly an instance of the 
specified class, otherwise False
"""

def is_same_class(obj, a_class):
    """Check if obj and a_class having
    the same class or not"""
    if type(obj) ==a_class:
        return True
    else:
        return False
