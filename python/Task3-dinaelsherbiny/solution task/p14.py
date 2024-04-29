
def smallest_sum(N, A):
    min_sum = float('inf')
    for i in range(N):
        for j in range(i + 1, N):
            current_sum = A[i] + A[j] + j - i
            min_sum = min(min_sum, current_sum)
    return min_sum


T = int(input())


for _ in range(T):

    N = int(input())
    A = list(map(int, input().split()))
    

    result = smallest_sum(N, A)
    
    print(result)
