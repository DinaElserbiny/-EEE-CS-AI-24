"""

Problem 2 
-write a program that takes today’s date and print tomorrow’s date
EX:
Input : Day : 1     Month: 4    Year: 2020
Output :  Day : 2     Month: 4    Year: 2020

"""

day = int (input("Day :"))
month = int (input("Month :"))
year = int (input("year :"))

month_31= [1,3,5,7,8,10,12] 
month_30=[4,6,9,11] 


if day==28 and month==2:
    if year%4 ==0:
        day=day+1
    else:
        day=1
        month=month+1

elif day==31 and month in month_31:
    if month ==12:
        day=1
        month=1
        year=year+1
    else:
        day=1
        month=month+1

elif day==30 and month in month_30:
    day=1
    month=month+1
else:
    day=day+1

print ("Day :",day ," ", "Month :",month," ","Year :",year )    


         

