#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        return 1

    result = 1
    base = a
    exponent = abs(b)

    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2

    return result if b >= 0 else 1 / result

if __name__ == "__main__":
    pow = __import__('1-pow').pow

    print(pow(2, 2))
    print(pow(98, 2))
    print(pow(98, 0))
    print(pow(100, -2))
    print(pow(-4, 5)) 
