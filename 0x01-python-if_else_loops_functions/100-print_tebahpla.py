#!/usr/bin/python3
result = ""
for i in range(ord('Z'), ord('A') - 1, -1):
    if i % 2 == 0:
        result += chr(i).lower()
    else:
        result += chr(i)
print(result, end="")
