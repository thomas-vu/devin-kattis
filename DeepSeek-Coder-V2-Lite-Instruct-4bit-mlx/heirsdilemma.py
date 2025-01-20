def is_valid(number):
    str_num = str(number)
    if len(set(str_num)) != 6:
        return False
    for digit in set(str_num):
        if int(digit) == 0 or number % int(digit) != 0:
            return False
    return True

def count_combinations(L, H):
    count = 0
    for num in range(L, H + 1):
        if is_valid(num):
            count += 1
    return count

# Read input
L, H = map(int, input().split())

# Output the result
print(count_combinations(L, H))