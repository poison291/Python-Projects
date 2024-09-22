def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers
    
    return fib_sequence

# Example usage
n = int(input("Enter the number of terms: "))
print(fibonacci(n))
