from fractions import Fraction
import re

def parse_input(line):
    parts = line.split()
    number_str, repeat_len = parts[0], int(parts[1])
    non_repeating, repeating = number_str.split('.')
    return (non_repeating + '.' + repeating), repeat_len

def find_fraction(number, repeat_len):
    if '.' not in number:
        return Fraction(int(number), 1)
    
    non_repeating, repeating = number.split('.')
    len_non_repeating = len(non_repeating)
    
    if repeat_len == 0:
        return Fraction(int(number), 10**len(repeating))
    
    numerator = int(non_repeating + repeating[:-repeat_len]) - int(non_repeating)
    denominator = int('9' * len(repeating[:-repeat_len]) + '0' * repeat_len)
    
    return Fraction(numerator, denominator)

def main():
    line = input().strip()
    number, repeat_len = parse_input(line)
    fraction = find_fraction(number, repeat_len)
    print(f"{fraction.numerator}/{fraction.denominator}")

if __name__ == "__main__":
    main()