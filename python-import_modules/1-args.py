import sys


if __name__ == "__main__":
    
    numbers = len(sys.argv) - 1

    # Print the number of arguments
    print("{} argument{}:".format(numbers, 's' if numbers != 1 else ''))

    if numbers == 0:
        # If no arguments were passed, print a dot and a new line
        print(":.")
    else:
        # Otherwise, print the arguments with their positions
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
