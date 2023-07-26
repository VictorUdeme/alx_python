def safe_print_division(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        result = None

    finally:
        print("Inside result:".format(result))

   
    safe_print_division(a, b)
        
    
    