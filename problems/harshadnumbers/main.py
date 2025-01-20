def is_harshad(num):
    sum_digits = sum([int(digit) for digit in str(num)])
    return num % sum_digits == 0

def next_harshad(n):
    num = n + 1
    while not is_harshad(num):
        num += 1
    return num

# Read input from stdin
n = int(input().strip())

# Output the smallest harshad number >= n
print(next_harshad(n))