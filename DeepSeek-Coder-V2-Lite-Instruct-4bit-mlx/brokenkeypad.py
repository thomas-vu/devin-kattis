def count_numbers_with_7(a, b):
    def contains_7(n):
        return '7' in str(n)
    
    count = 0
    for number in range(a, b + 1):
        if contains_7(number):
            count += 1
    return count

# Sample Input 1
a, b = 1, 10
print(count_numbers_with_7(a, b))  # Sample Output 1

# Sample Input 2
a, b = 8, 160
print(count_numbers_with_7(a, b))  # Sample Output 2

# Sample Input 3
a, b = 700, 7777
print(count_numbers_with_7(a, b))  # Sample Output 3