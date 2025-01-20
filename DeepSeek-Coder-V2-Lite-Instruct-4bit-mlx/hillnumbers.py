def is_hill_number(n):
    s = str(n)
    rise = False
    fall = False
    
    for i in range(1, len(s)):
        if s[i] > s[i - 1]:
            rise = True
        elif s[i] < s[i - 1]:
            if rise:
                fall = True
        else:
            return False
    
    return True if rise and (not fall or len(s) == 1) else False

def count_hill_numbers(n):
    if not is_hill_number(n):
        return -1
    
    def count_up_to(digits, pos, prev, rise):
        if pos == len(digits):
            return 1
        
        count = 0
        for digit in range(prev if pos == 0 else 0, 10):
            if rise and digit > int(digits[pos]):
                break
            count += count_up_to(digits, pos + 1, digit, rise and (digit < int(digits[pos])))
        
        return count
    
    digits = str(n)
    return count_up_to(digits, 0, 0, True)

# Read input
n = int(input())
if is_hill_number(n):
    print(count_hill_numbers(n))
else:
    print(-1)