def probability_distribution(data):
    total_count = len(data)
    value_counts = {}
    for value in data:
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1
    for value in value_counts:
        value_counts[value] /= total_count
    return value_counts

# Example usage:
data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1]
print(probability_distribution(data))
# Output: {1: 0.3, 2: 0.2, 3: 0.2, 4: 0.2, 5: 0.1}
