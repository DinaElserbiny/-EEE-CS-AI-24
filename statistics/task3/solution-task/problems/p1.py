def calculate_statistics(count):
    total_count = sum(count)
    
    # Minimum and Maximum
    minimum = next(i for i in range(len(count)) if count[i] > 0)
    maximum = next(i for i in range(len(count) - 1, -1, -1) if count[i] > 0)
    
    # Mean
    mean = sum(i * count[i] for i in range(len(count))) / total_count
    
    # Median
    cumulative_count = 0
    if total_count % 2 == 1:
        median_index = total_count // 2
        median = next(i for i in range(len(count)) if (cumulative_count := cumulative_count + count[i]) > median_index)
    else:
        median_index = total_count // 2
        prev_count = 0
        for i in range(len(count)):
            cumulative_count += count[i]
            if cumulative_count >= median_index:
                if cumulative_count > median_index:
                    median = i
                else:
                    next_index = next(j for j in range(i + 1, len(count)) if count[j] > 0)
                    median = (i + next_index) / 2
                break
    
    # Mode
    mode = count.index(max(count))
    
    return [minimum, maximum, mean, median, mode]

def main():
    count_str = input("Enter the count array (comma-separated integers): ")
    count = list(map(int, count_str.split(',')))
    
    statistics = calculate_statistics(count)
    print("Statistics of the sample:")
    print("Minimum:", statistics[0])
    print("Maximum:", statistics[1])
    print("Mean:", statistics[2])
    print("Median:", statistics[3])
    print("Mode:", statistics[4])

if __name__ == "__main__":
    main()
