#!/usr/bin/python3
"""
Module for reading and printing text files.

This module provides functionality to read UTF-8 encoded text files
and print their contents to standard output.
"""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print it to stdout.

    Args:
        filename (str): The path to the file to read. Defaults to empty string.

    The function uses the 'with' statement to ensure proper file handling
    and automatically closes the file after reading.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content, end='')
