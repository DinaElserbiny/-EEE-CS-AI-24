

N = int(input())
A = list(map(int, input().split()))



def all_even(arr):
    for num in arr:
        if num % 2 != 0:
            return False
    return True


operations = 0
while all_even(A):
    operations += 1
    A = [num // 2 for num in A]


print(operations)
