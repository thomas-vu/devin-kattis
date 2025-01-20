def min_days_to_print_statues(n):
    days = 0
    while n > 1:
        if n % 2 == 1:
            n = (n + 1) // 2
        else:
            n //= 2
        days += 1
    return days + 1 if n == 1 else days

# Read input from stdin
n = int(input().strip())
print(min_days_to_print_statues(n))