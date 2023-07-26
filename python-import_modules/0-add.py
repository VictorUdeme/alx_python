# File: main.py

a = 1
b = 2

# Import the 'add_0' module
import add_0

# Calculate the result using the 'add' function from 'add_0' module
result = add_0.add(a, b)

# Print the result using .format() to display the values
print("{a} + {b} = {result}".format(a=a, b=b, result=result))

if __name__ == "__main__":
    pass

