import sys

def print_arguments():
    argv = sys.argv[1:]
    num_args = len(argv)

    print(f"{num_args} argument{'s' if num_args != 1 else ''}{':' if num_args > 0 else '.'}")

    if num_args > 0:
        for i, arg in enumerate(argv, 1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments()
