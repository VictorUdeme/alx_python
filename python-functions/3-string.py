def reverse_string(string):

    reversed_str = ""

    
    for i in range(len(string) - 1, -1, -1):
       
        reversed_str += string[i]

    return reversed_str
reverse_string = __import__('3-string').reverse_string

print(reverse_string("Hello"))         
print(reverse_string(""))             
print(reverse_string("madam"))         
print(reverse_string("Hello, World!"))