def hailstone_sequence_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

# Example usage:
n = int(input())
print(hailstone_sequence_length(n))