
def max_subarray(arr):
    n = len(arr)
    result = []
    for i in range(n):
        max_num = float('-inf')
        for j in range(i, n):
            max_num = max(max_num, arr[j])
            result.append(max_num)
    return result


T = int(input())


for _ in range(T):

    N = int(input())
    A = list(map(int, input().split()))
    

    max_numbers = max_subarray(A)
    

    print(*max_numbers)
