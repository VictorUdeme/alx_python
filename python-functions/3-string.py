def reverse_string(string):

    reverse_string = ""

    
    for i in range(len(string) - 1, -1, -1):
       
        reverse_string += string[i]

    return reverse_string

reverse_string = __import__('3-string').reverse_string
print(repr(reverse_string("Hello")))         
print(repr(reverse_string("")))            
print(repr(reverse_string("madam")))        
print(repr(reverse_string("Hello, World!")))
