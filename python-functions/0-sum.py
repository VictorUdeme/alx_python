def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

if __name__ == "__main__":
    add = __import__('0-sum').add

