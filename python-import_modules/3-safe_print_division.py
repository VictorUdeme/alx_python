def safe_print_division(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        result = None

    finally:
        print("Inside result:".format(result))

    a = 9
    b = 3
    safe_print_division(a, b)
        
    
    