#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Returns a new list with all occurrences of search replaced by replace."""
    new_list = [replace if x == search else x for x in my_list]
    return new_list
