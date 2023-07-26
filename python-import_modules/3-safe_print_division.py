def safe_print_division(a, b):
    try:
        result = (a) / (b)
    except ZeroDivisionError:
        result = None
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
            print("{} / {} = {}".format(a, b, result))
        else:
            print("Inside result: None")
        
