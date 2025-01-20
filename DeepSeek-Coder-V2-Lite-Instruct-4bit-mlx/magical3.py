def find_smallest_base(n):
    for base in range(2, 37):
        representation = convert_to_base(n, base)
        if representation.endswith('3'):
            return base
    return "No such base"

def convert_to_base(n, base):
    if n < base:
        return str(n)
    else:
        digits = []
        while n > 0:
            remainder = n % base
            if remainder < 10:
                digits.append(chr(ord('0') + remainder))
            else:
                digits.append(chr(ord('A') + remainder - 10))
            n //= base
        return ''.join(reversed(digits))

while True:
    n = int(input())
    if n == 0:
        break
    print(find_smallest_base(n))