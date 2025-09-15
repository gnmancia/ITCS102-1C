import random

# Generate 10 random numbers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(10)]

print("Generated numbers:", numbers)

# Variable to store sum of odd numbers
odd_sum = 0

# Loop through numbers
for num in numbers:
    if num % 2 != 0:  # check if odd
        odd_sum += num

print("Sum of odd numbers:", odd_sum)
