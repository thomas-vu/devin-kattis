def hailstone_sum(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + hailstone_sum(n // 2)
    else:
        return n + hailstone_sum(3 * n + 1)

# Example usage:
print(hailstone_sum(5))  # Output: 36
print(hailstone_sum(7))  # Output: 288