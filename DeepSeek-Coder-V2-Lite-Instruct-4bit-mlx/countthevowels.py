def count_vowels(s):
    vowels = "AEIOUaeiou"
    return sum(1 for char in s if char in vowels)

# Read input from stdin
s = input().strip()

# Output the number of vowels in the string
print(count_vowels(s))