#!/usr/bin/env python3
def add(a, b):
   
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

print(__import__('0-sum').add(1, 2))
print(__import__('0-sum').add(98, 0))
print(__import__('0-sum').add(100, -2))
 