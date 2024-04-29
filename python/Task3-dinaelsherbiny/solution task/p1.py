"""
O. Fibonacci
link : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/O

"""




def fac(n):
    if n==2:
       return 1
    if n==1:
     return 0
    elif n>=3:
        return fac (n-1)+fac(n-2)

n=int(input(""))
result = fac(n)
print(result)
