"""
Problem 1 
-Write a program that takes any numbers from user terminates if user enters -1  
then prints largest and smallest number
EX:
Input : 5 9 12 100 3 8 0 -1
Output : 100 0

"""

num = int(input("Enter num :" ))
max=min= num
while num != -1:
    if num ==-1:
        break
    num=int(input("Enter num :" )) 
    if max <num and num != -1:
       max=num
    elif min >num and  num != -1:
        min=num

print(max," ",min)           