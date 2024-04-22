"""

"""
def knapsack(items, capacity, n):

    if n == 0 or capacity == 0:
        return 0


    if items[n - 1][0] > capacity:
        return knapsack(items, capacity, n - 1)

    
    return max(items[n - 1][1] + knapsack(items, capacity - items[n - 1][0], n - 1),
               knapsack(items, capacity, n - 1))

N, W = map(int, input().split())

items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

max_value = knapsack(items, W, N)
print(max_value)
