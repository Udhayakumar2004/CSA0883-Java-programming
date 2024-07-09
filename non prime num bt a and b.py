import math

def is_prime(num):
    """ Function to check if a number is prime """
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # other even numbers are not prime
    # check for odd factors from 3 up to the square root of num
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def print_non_prime_numbers(a, b):
    """ Function to print non-prime numbers between a and b """
    for num in range(a, b + 1):
        if not is_prime(num):
            print(num, end=" ")

# Example usage:
a = 900
b = 1000
print(f"Non-prime numbers between {a} and {b}:")
print_non_prime_numbers(a, b)
