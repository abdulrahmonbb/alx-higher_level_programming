#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    largest = None
    for num in my_list:
        if largest is None or num > largest:
            largest = num
    return largest 
