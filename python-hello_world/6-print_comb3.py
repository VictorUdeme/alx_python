for tens_digit in range(0, 10):
    for units_digit in range(tens_digit + 1, 10):
        print("{:01d}{:01d}".format(tens_digit, units_digit), end=", " if tens_digit < 8 else "\n")
