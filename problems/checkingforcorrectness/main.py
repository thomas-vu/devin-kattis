#!/usr/bin/env python3

def mod_pow(base, exp, modulus):
    result = 1
    base %= modulus
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % modulus
        exp >>= 1
        base = (base * base) % modulus
    return result

def last_four_digits(num):
    num %= 10000
    return num if num != 0 else "0"

import sys
for line in sys.stdin:
    parts = line.split()
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    
    if op == '+':
        result = (a + b) % 10000
    elif op == '*':
        result = (a * b) % 10000
    elif op == '^':
        result = mod_pow(a, b, 10000)
    
    print(last_four_digits(result))