#!/usr/bin/python3
if __name__ == "__main__":
    """Print result of a and b"""
    from add_0 import add
    a = 1
    b = 2
    result = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))
