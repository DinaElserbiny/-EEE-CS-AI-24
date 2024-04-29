
A, B = map(int, input().split())
S = input()


def check_code(A, B, S):

    if len(S) != A + B + 1:
        return "No"
    

    if S[A] != '-':
        return "No"
    

    for i in range(A + B + 1):
        if i != A and not S[i].isdigit():
            return "No"
    
    return "Yes"


print(check_code(A, B, S))
