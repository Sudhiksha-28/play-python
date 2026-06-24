def largest_prime_factor(n):
    # Step 1: Remove all factors of 2
    while n % 2 == 0:
        max_prime = 2
        n //= 2
        
    # Step 2: Check odd numbers up to the square root of n
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            max_prime = factor
            n //= factor
        factor += 2
        
    # Step 3: If n is still greater than 2, then n itself is prime
    if n > 2:
        max_prime = n
        
    return max_prime

# Example Usage:
number = 13195
print(f"The largest prime factor of {number} is: {largest_prime_factor(number)}")

# Test with a massive number (like the Project Euler #3 problem)
large_number = 600851475143
print(f"The largest prime factor of {large_number} is: {largest_prime_factor(large_number)}")