def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def test_conversion(input_fahrenheit, expected_celsius):
    result = convert_to_celsius(input_fahrenheit)
    tolerance = 1e-9
    if abs(result - expected_celsius) > tolerance:
        raise AssertionError(f"Expected {expected_celsius}, but got {result}")

test_conversion(100, 37.77777777777778)
test_conversion(-40, -40.0)
test_conversion(-459.67, -273.15)
test_conversion(32, 0.0)
