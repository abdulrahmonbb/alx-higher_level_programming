#!/usr/bin/python3
def remove_char_at(str, n):
<<<<<<< HEAD
    str[n] = ""
    return str
=======
    if n < 0:
        return str
    return str[:n] + str[n+1:]
>>>>>>> 36ffdc376cec77c3ca502faf92388329c8a636ad
