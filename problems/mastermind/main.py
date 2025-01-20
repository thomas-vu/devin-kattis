def calculate_feedback(code, guess):
    r = 0
    s = 0
    code_count = [0] * 26
    guess_count = [0] * 26
    
    for i in range(len(code)):
        if code[i] == guess[i]:
            r += 1
        else:
            code_count[ord(code[i]) - ord('A')] += 1
            guess_count[ord(guess[i]) - ord('A')] += 1
    
    for i in range(26):
        s += min(code_count[i], guess_count[i])
    
    return r, s

# Read input
n = int(input().strip())
code = input().strip()
guess = input().strip()

# Calculate feedback
r, s = calculate_feedback(code, guess)

# Output the result
print(r, s)