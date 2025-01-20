def can_always_guess(s):
    letter_count = {}
    for letter in s:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    
    odd_counts = sum(1 for count in letter_count.values() if count % 2 != 0)
    
    return 1 if odd_counts <= 2 else 0

# Read input from stdin
s = input().strip()
print(can_always_guess(s))