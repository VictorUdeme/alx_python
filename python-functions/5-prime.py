def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test cases and expected outputs
test_cases = [17, 15, -5, 0]
expected_outputs = [True, False, False, False]

# Run the test cases and compare with expected outputs
for i in range(len(test_cases)):
    result = is_prime(test_cases[i])
    expected = expected_outputs[i]
    assert result == expected, f"Test case {test_cases[i]} failed. Expected: {expected}, Got: {result}"
