
"""
Problem 8
-Write a Python program that takes a positive integer as input and checks whether it is a
perfect number or not. A perfect number is a positive integer that is equal to the sum of its
proper divisors, excluding itself.
EX:
Input: 28
Output: 28 is a perfect numb
"""


num = int(input("Enter a positive integer: "))


divisors_sum = 0
for i in range(1, num):
    if num % i == 0:
        divisors_sum += i


if divisors_sum == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
