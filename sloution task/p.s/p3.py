"""
Problem 3
Write a Python program that takes a positive integer as input and calculates its factorial.
Input: 5
Output: The factorial of 5 is 120 (5 * 4 * 3 * 2 * 1).


"""
num= int(input("Enter num :"))
fac=1
for i in range(2,num+1):
   fac =fac*i

print ("The factorial of ",num, "is ",fac )