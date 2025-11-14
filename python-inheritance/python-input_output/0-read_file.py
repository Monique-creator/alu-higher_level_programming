#!/usr/bin/python3
"""
Module for reading and printing text files
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    
    Args:
        filename: path to the file to read (default: empty string)
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
