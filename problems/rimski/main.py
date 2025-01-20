def smallest_roman(B):
    roman_numerals = {10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC'}
    ones = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    
    tens = B // 10 * 10
    ones_digit = B % 10
    
    if tens == 40:
        return 'XL' + ones[ones_digit]
    elif tens == 90:
        return 'XC' + ones[ones_digit]
    else:
        if tens > 0 and ones_digit > 0:
            return roman_numerals[tens] + ones[ones_digit]
        else:
            return roman_numerals.get(tens, '') + ones.get(ones_digit, '')

# Read input
B = int(input())
print(smallest_roman(B))