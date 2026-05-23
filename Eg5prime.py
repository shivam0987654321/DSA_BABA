# Prime number check

# Brute Force - Check if prime
def is_prime_brute(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False  # Found a divisor, not prime
    return True  # No divisors found

num = 12
result = is_prime_brute(num)
print(f"{num} is prime: {result}")  # False

# Best solution - Optimized (only check up to sqrt)
def is_prime_optimized(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num1 = 13
result1 = is_prime_optimized(num1)
print(f"{num1} is prime: {result1}")  # True



