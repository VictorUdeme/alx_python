def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci_numbers = [0, 1]
    for _ in range(2, n):
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        if next_number <= 0:  # Check for integer overflow
            return []
        fibonacci_numbers.append(next_number)
    
    return fibonacci_numbers

print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))
