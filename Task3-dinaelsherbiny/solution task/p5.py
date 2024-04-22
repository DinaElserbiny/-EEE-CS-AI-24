"""
Q. 3n + 1 sequence
https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/Q
"""
def seq(num,c=0):
 if num<=1:
  return c+1
 
 else:
    if num%2==0:
        num=num/2
        return seq(num,c+1) 
        
    else:
        num=3*num+1
        return seq(num,c+1)



num=int(input())
print(seq(num))