def fraction_to_decimal(numerator, denominator):
    if numerator % denominator == 0:
        return (0, 0)
    
    decimal_part = []
    index_map = {}
    remainder = numerator % denominator
    integer_part = numerator // denominator
    
    while remainder != 0:
        if remainder in index_map:
            index = index_map[remainder]
            non_repeating = decimal_part[:index]
            repeating = decimal_part[index:]
            return (len(non_repeating), len(repeating))
        index_map[remainder] = len(decimal_part)
        remainder *= 10
        decimal_part.append(remainder // denominator)
        remainder %= denominator
    
    return (len(decimal_part), 0)

# Read input from stdin
import sys
input = sys.stdin.readline
numerator, denominator = map(int, input().split())
f, i = fraction_to_decimal(numerator, denominator)
print(f, i)