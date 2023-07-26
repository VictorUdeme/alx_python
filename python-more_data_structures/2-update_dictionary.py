def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return

    keys = sorted(a_dictionary.keys())
    for key in keys:
        value = a_dictionary[key]
        print(f"{key}: {value}")