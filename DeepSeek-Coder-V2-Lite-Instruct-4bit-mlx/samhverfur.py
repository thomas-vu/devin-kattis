def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_largest_palindrome(limit):
    for num in range(limit, 0, -1):
        if is_palindrome(num):
            return num
    return 0

results = []
for k in range(1, 101):
    power_of_two = 2 ** k
    largest_palindrome = find_largest_palindrome(power_of_two)
    results.append((k, largest_palindrome))

for k, palindrome in results:
    print(f"{k} {palindrome}")