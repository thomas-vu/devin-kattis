def alien_to_decimal(alien_number, source_language):
    base = len(source_language)
    decimal_value = 0
    for digit in alien_number:
        decimal_value = decimal_value * base + source_language.index(digit)
    return decimal_value

def decimal_to_alien(decimal_number, target_language):
    if decimal_number == 0:
        return target_language[0]
    alien_digits = []
    base = len(target_language)
    while decimal_number > 0:
        digit = decimal_number % base
        alien_digits.append(target_language[digit])
        decimal_number //= base
    return ''.join(reversed(alien_digits))

def main():
    T = int(input())
    for x in range(1, T + 1):
        alien_number, source_language, target_language = input().split()
        decimal_value = alien_to_decimal(alien_number, source_language)
        translated_number = decimal_to_alien(decimal_value, target_language)
        print("Case #{}: {}".format(x, translated_number))

if __name__ == "__main__":
    main()