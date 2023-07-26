import sys

if __name__ == "__main__":
    number = len(sys.argv)
    print("Number of argument(s):", number)

    if number == 0:
        print(": .")
    else:
        print("arguments:", end="")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("\n{}: {}" .format(i,arg))