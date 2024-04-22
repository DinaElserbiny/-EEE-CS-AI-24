
def is_subsequence(A, B):

    i = 0 
    j = 0  


    while i < len(A) and j < len(B):

        if A[i] == B[j]:
            j += 1

        i += 1


    return j == len(B)


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


if is_subsequence(A, B):
    print("YES")
else:
    print("NO")
