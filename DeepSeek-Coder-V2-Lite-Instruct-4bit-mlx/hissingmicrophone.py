def check_hiss(word):
    for i in range(len(word) - 1):
        if word[i] == 's' and word[i + 1] == 's':
            return "hiss"
    return "no hiss"

# Read input from stdin
word = input().strip()

# Output the result
print(check_hiss(word))