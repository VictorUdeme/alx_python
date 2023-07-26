a = 1
b = 2

# The following block ensures the code is non-executable when imported
if __name__ == "__main__":
    # Import the 'add' function from add_0.py
    from add_0 import add

   
    print("{a} + {b} = {result}".format(a=a, b=b, result=add(a, b)))
