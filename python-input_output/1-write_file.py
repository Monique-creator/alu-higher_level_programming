#!/usr/bin/python3
"""
Module 1-write_file
Defines a function that writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return
    the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

