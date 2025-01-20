def count_walks(n):
    if n == 0:
        return 1
    elif n == 1:
        return 6
    else:
        # Initialize the number of walks for n = 0 and n = 1
        a, b = 6, 6
        for _ in range(2, n + 1):
            a, b = b, 6 * (a + b)
        return b

# Read the number of test cases
num_test_cases = int(input())
for _ in range(num_test_cases):
    n = int(input())
    print(count_walks(n))