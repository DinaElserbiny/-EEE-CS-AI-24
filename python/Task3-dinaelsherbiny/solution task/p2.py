"""
B. Print from 1 to N
link : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/B

"""


def fac(n,m=1):
    
    if m==n:
      print(m)
      return 

    else:
        print (m)
        return fac(n,m+1)


n=int(input(""))
fac(n)

