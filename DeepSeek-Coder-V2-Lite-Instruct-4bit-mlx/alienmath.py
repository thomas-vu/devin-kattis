def alien_to_decimal(base, digits, number):
    digit_map = {digit: i for i, digit in enumerate(digits)}
    decimal_value = 0
    power = 0
    
    for digit in reversed(number):
        decimal_value += digit_map[digit] * (base ** power)
        power += 1
    
    return decimal_value

# Read input
base = int(input())
digits = input().split()
number = input()

# Convert and print the result
print(alien_to_decimal(base, digits, number))