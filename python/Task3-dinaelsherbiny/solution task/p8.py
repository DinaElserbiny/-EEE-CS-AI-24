"""

"""
def max_path_sum(matrix, i, j, N, M):

    if i == N - 1 and j == M - 1:
        return matrix[i][j]


    if i >= N or j >= M:
        return float('-inf')


    
    
    down_sum = max_path_sum(matrix, i + 1, j, N, M)
    right_sum = max_path_sum(matrix, i, j + 1, N, M)


    return matrix[i][j] + max(down_sum, right_sum)


N, M = map(int, input().split())


matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)


result = max_path_sum(matrix, 0, 0, N, M)
print(result)
