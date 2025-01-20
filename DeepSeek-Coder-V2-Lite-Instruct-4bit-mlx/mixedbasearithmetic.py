def increment_counter(c, i):
    # Helper function to handle the character part of the counter
    def increment_char(ch):
        if 'a' <= ch <= 'z':
            return chr(((ord(ch) - ord('a') + i) % 26) + ord('a'))
        elif 'A' <= ch <= 'Z':
            return chr(((ord(ch) - ord('A') + i) % 26) + ord('A'))
        else:
            return ch
    
    # Helper function to handle the numeric part of the counter
    def increment_digit(d):
        return str((int(d) + i) % 10)
    
    # Separate the alphabetic and numeric parts of the counter
    chars = [ch for ch in c if not ch.isdigit()]
    digits = [d for d in c if d.isdigit()]
    
    # Increment the alphabetic part first (from right to left)
    for j in range(len(chars)-1, -1, -1):
        chars[j] = increment_char(chars[j])
    
    # If all alphabetic parts are fully carried, add a new digit of the same type as the previous high-order digit
    if all(ch.isalpha() for ch in chars):
        new_digit = 'a' if chars[-1].islower() else 'A'
        chars.append(new_digit)
    
    # Increment the numeric part from right to left
    for j in range(len(digits)-1, -1, -1):
        digits[j] = increment_digit(digits[j])
        i = 0  # Reset the carry for each digit
    
    # Combine the parts back into a single string
    result = ''.join(chars) + ''.join(digits)
    return result

# Read input until EOF
while True:
    try:
        c, i = input().split()
        i = int(i)
    except EOFError:
        break
    
    # Increment the counter i times
    for _ in range(i):
        c = increment_counter(c, 1)
    
    print(c)