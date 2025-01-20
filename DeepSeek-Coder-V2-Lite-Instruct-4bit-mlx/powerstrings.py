def find_largest_exponent(s):
    for n in range(len(s), 0, -1):
        if len(s) % n == 0:
            substring = s[:len(s) // n]
            if substring * (len(s) // len(substring)) == s:
                return n
    return 1

while True:
    s = input().strip()
    if s == '.':
        break
    print(find_largest_exponent(s))