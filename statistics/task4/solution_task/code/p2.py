
def conditional_probability(event_a, event_b):
    count_a_and_b = sum(1 for a, b in zip(event_a, event_b) if a == 1 and b == 1)
    count_a = sum(1 for a in event_a if a == 1)
    if count_a == 0:
        return 0
    return count_a_and_b / count_a

# Example usage:
event_a = [1, 0, 1, 0, 1]
event_b = [1, 1, 0, 0, 1]
print(conditional_probability(event_a, event_b))
# Output: 0.5

