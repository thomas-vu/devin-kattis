def next_price(digits):
    digits = list(digits)
    n = len(digits) - 1
    
    # Find the first digit that can be increased
    i = n - 1
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    if i == -1:
        return "The price cannot be raised"
    
    # Find the smallest digit larger than digits[i] to swap with
    j = i + 1
    while j < n and digits[j] > digits[i]:
        j += 1
    j -= 1
    
    # Swap the digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]
    
    # Reverse the subarray from i+1 to n
    digits[i + 1:] = reversed(digits[i + 1:])
    
    return ''.join(digits)

while True:
    line = input()
    if line == '.':
        break
    print(next_price(line))