#!/usr/bin/python3
"""
Module 1-my_list
Defines a class MyList that inherits from list
"""

class MyList(list):
    """Custom list class that inherits from list"""

    def print_sorted(self):
        """Print the list, but sorted in ascending order"""
        print(sorted(self))

