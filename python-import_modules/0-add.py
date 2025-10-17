#!/usr/bin/python3
"""Print the sum of 1 + 2 using add_0.add function."""

if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))

