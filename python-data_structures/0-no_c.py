def no_c(my_string):
   if len(my_string) == 0:
        return my_string
   new_string = ""
   if my_string[0] == "S":
    new_string += "S"
   for character in my_string[1:]:
    if character != "c" and character != "C":
      new_string += character

   return new_string
