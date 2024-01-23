#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for elem in my_list:
            if count < x:
                print(elem, end=' ')
                count+=1
            else:
                break

        print()
        return count
    except:
        print("An error occured while printing")
        return (0)
