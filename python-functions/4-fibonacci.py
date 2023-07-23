def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        if next_number <= 0: 
            return []
        fibonacci_numbers.append(next_number)
    
    return fibonacci_numbers
if __name__ == "__main__":
    fibonacci_sequence = __import__('4-fibonacci').fibonacci_sequence
