def roman_to_int(roman):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(roman):
        value = values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def main():
    n = int(input())
    numbers = []
    for _ in range(n):
        number = int(input())
        numbers.append(number)
    
    roman_order = []
    i = 1
    while True:
        roman_num = int_to_roman(i)
        if i > 10**9:
            break
        roman_order.append(roman_num)
        i += 1
    
    for number in numbers:
        roman_num = int_to_roman(number)
        position = roman_order.index(roman_num) + 1
        if number == int(''.join(sorted(roman_num, reverse=True))):
            position = -position
        print(position)

if __name__ == "__main__":
    main()