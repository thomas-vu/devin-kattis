def min_days_to_certify(binary_str):
    n = len(binary_str)
    days = 0
    while '0' in binary_str:
        new_str = ''
        for i in range(n):
            if binary_str[i] == '0':
                continue
            if i > 0 and binary_str[i-1] == '0':
                continue
            if i < n - 1 and binary_str[i+1] == '0':
                continue
            new_str += '0'
        binary_str = new_str
        days += 1
    return days

# Read input from stdin
binary_str = input().strip()
print(min_days_to_certify(binary_str))