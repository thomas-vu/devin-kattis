def average_ascii(s):
    total = sum(ord(c) for c in s)
    average_value = int(total / len(s))
    return chr(average_value)

# Sample Input 1
s = "ABCDE"
print(average_ascii(s))  # Sample Output 1

# Sample Input 2
s = "AbCdE"
print(average_ascii(s))  # Sample Output 2

# Sample Input 3
s = "aBcDeV"
print(average_ascii(s))  # Sample Output 3