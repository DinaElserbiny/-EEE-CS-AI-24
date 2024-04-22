

from collections import Counter

# Input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Count the frequency of elements in both arrays
count_A = Counter(A)
count_B = Counter(B)

# Check if both arrays have the same elements with the same frequency
if count_A == count_B:
    print("yes")
else:
    print("no")
