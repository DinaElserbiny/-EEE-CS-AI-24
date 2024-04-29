
def count_divisors(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            if num // i == i:
                count += 1
            else:
                count += 2
    return count


N = int(input())
A = list(map(int, input().split()))


print("The maximum number:", max(A))
print("The minimum number:", min(A))


prime_count = sum(1 for num in A if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)))
print(prime_count)


palindrome_count = sum(1 for num in A if str(num) == str(num)[::-1])
print(palindrome_count)


max_divisors = max(A, key=count_divisors)
print(max_divisors)
