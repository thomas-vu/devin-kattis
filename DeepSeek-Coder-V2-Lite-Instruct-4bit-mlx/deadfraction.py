import sys

def decimal_to_fraction(decimal):
    if '...' in decimal:
        decimal = decimal.replace('...', '')
    else:
        return int(decimal), 1
    
    non_repeating, repeating = decimal.split('...')
    if non_repeating:
        non_repeating = int(non_repeating)
    else:
        non_repeating = 0
    
    repeating = repeating.lstrip('0')
    if not repeating:
        return non_repeating, 10**len(decimal.split('.')[1])
    
    length_repeating = len(repeating)
    length_non_repeating = len(str(non_repeating)) if non_repeating else 0
    
    denominator = (10**(length_repeating) - 1) * (10**(len(decimal.split('.')[1]) - length_repeating) if non_repeating == 0 else (10**(len(decimal.split('.')[1]) - length_repeating) - 10**length_non_repeating)
    numerator = int(str(non_repeating) + repeating) * denominator
    
    gcd = find_gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

for line in sys.stdin:
    if line.strip() == '0':
        break
    numerator, denominator = decimal_to_fraction(line.strip())
    print(f"{numerator}/{denominator}")