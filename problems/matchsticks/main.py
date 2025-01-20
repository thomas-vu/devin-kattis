def smallest_and_largest(n):
    if n == 2:
        return "1 1"
    elif n == 3:
        return "7 7"
    elif n == 4:
        return "111 711"
    elif n == 5:
        return "77 771"
    elif n == 6:
        return "11111 7111"
    elif n == 7:
        return "7771 7771"
    elif n == 8:
        return "1111111 711111"
    elif n == 9:
        return "777771 777771"
    elif n == 10:
        return "7111111 7111111"
    else:
        return "Invalid input"

# Read the number of test cases
t = int(input())
for _ in range(t):
    n = int(input())
    result = smallest_and_largest(n)
    print(result)