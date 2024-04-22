"""
D. Print Digits using Recursion
https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/D

"""


def print_digits(n):
    if n < 10:
        print(n, end=' ')
    else:
       print_digits(n // 10)
       print(n % 10, end=' ')




t = int(input())


for _ in range(t):
    num = int(input())
    print_digits(num)
    print()  
    