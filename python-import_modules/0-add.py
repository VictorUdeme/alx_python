a = 1
b = 2

# The following block ensures the code is non-executable when imported
if __name__ == "__main__":
    # Import the 'add' function from add_0.py
    from add_0 import add

   
    print("{} + {} = {}".format(a, b, add(a, b)))
