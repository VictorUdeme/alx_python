def add(a, b):
    for _ in range(b):
        a -= 1

    return a
add = __import__('0-sum').add