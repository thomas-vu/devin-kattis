def count_liked_numbers(n):
    n = str(n)
    liked_count = 0
    
    for i in range(len(n)):
        if n[i] == '0':
            liked_count += 1
        elif n[i] == '2':
            liked_count += 1
    
    return liked_count

# Sample Input 1
n = 102
print(count_liked_numbers(n))  # Sample Output 1

# Sample Input 2
n = 2217
print(count_liked_numbers(n))  # Sample Output 2

# Sample Input 3
n = 12345632
print(count_liked_numbers(n))  # Sample Output 3