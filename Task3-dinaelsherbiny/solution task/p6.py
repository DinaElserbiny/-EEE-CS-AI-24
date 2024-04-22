"""

"""



def can_reach(N, current):

    if current == N:
        return True
          
    elif current > N:
        return False

    else:
        if can_reach(N, current * 10):
            return True
        
        if can_reach(N, current * 20):
            return True
        return False

def solve_test_case(N):
    if can_reach(N, 1):
        print("YES")
    else:
        print("NO")

T = int(input())

for _ in range(T):
    N = int(input()) 
    solve_test_case(N)
