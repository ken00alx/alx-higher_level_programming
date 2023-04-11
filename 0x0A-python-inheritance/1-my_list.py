#!/usr/bin/python3
"""
Module with class Mylist
"""

class Mylist(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Method of sorting a list"""
        
        print(sorted(list(self)))
