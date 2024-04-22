

N = int(input())
A = list(map(int, input().split()))


min_num = min(A)
max_num = max(A)
min_index = A.index(min_num)
max_index = A.index(max_num)


A[min_index], A[max_index] = A[max_index], A[min_index]



print(*A)
