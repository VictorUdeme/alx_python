def no_c(my_string):
    new_string = ""
    for x in my_string:
        if x != "c" and x != "C":
            new_string += my_string
    return new_string
