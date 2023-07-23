def add(a, b):
    if b>= 0:
        for _ in range(b):
         a += 1

    else:
       for _ in range(abs(b)):
          a -= 1
    return a

add = __import__('0-sum').add