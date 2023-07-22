def reverse_string(string):

    reversed_str = ""

    
    for i in range(len(string) - 1, -1, -1):
       
        reversed_str += string[i]

    return reversed_str


print(repr(reverse_string("Hello")))         
print(repr(reverse_string("")))            
print(repr(reverse_string("madam")))        
print(repr(reverse_string("Hello, World!")))
