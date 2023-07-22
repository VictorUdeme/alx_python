def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

if __name__ == "__main__":
    add = __import__('0-sum').add

    print(add(1, 2))  
    print(add(98, 0))
    print(add(100, -2)) 
