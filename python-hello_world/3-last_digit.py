#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = (number) % 10
output = "Last digit of " + str(number) + " is " + str(Last_digit)
if Last_digit > 5:
    print (output, "and is greater than 5")
elif Last_digit == 0:
    print(output, "and is 0")
else:
    print(output, "and is less than 6 and not 0")
