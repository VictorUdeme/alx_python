for tens_digit in range(0, 10):
    for units_digit in range(tens_digit + 1, 10):
        print(f"{tens_digit:01d}{units_digit:01d}", end=", ")
