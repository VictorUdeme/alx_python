import sys

if __name__ == "__main__":
    number = len(sys.argv)
    print("{} argument{}:".format(number, 's' if number != 1 else ''), end='')

    if number == 0:
        print("\n:.")
   
    else:
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("\n{}: {}" .format(i, arg))