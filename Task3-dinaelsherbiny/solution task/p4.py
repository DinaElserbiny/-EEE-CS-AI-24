"""
S. Array Average
https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/S
"""

def array_average(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + array_average(arr, n - 1)

n = int(input())
arr = [int(x) for x in input().split()]
total_sum = array_average(arr, n)
average = total_sum / n
print("{:.6f}".format(average))
