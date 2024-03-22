"""

Problem 6
-Write a Python program that takes a positive integer as input and calculates the sum of all even numbers from 1 to that integer.
Input: 6
Output: The sum of even numbers from 1 to 6 is 12 (2 + 4 + 6).

"""
num =int(input("Enter num :"))
sum=0
for i in range(0,num+1,2):
    sum=sum+i
print("The sum of even numbers from 1 to",num,"is ",sum)
