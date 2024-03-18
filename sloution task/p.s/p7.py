"""
Problem 7
-Write a Python program that takes a positive integer as input and finds its prime factors.
Input: 36
Output: Prime Factors: 2, 3
"""


num = int(input("Enter a positive integer: "))

factors = []


while num % 2 == 0:
    factors.append(2)
    num //= 2


for i in range(3, int(num**0.5) + 1, 2):
    while num % i == 0:
        factors.append(i)
        num //= i


if num > 2:
    factors.append(num)

# Printing the result
print("Prime Factors:", ', '.join(map(str, factors)))
