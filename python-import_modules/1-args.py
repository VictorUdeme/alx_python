import sys

# The following block ensures the code is non-executable when imported
if __name__ == "__main__":
    # Get the number of arguments
    num_arguments = len(sys.argv) - 1

    # Print the number of arguments
    print("{} argument{}.".format(num_arguments, '' if num_arguments == 1 else 's'))

    # Print the list of arguments with their positions
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
