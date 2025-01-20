def sexagesimal_to_decimal(sexagesimal):
    digits = [int(x) for x in sexagesimal.split(',')]
    decimal_value = 0
    power = len(digits) - 1
    for digit in digits:
        decimal_value += digit * (60 ** power)
        power -= 1
    return decimal_value

def main():
    N = int(input())
    for _ in range(N):
        sexagesimal_number = input()
        print(sexagesimal_to_decimal(sexagesimal_number))

if __name__ == "__main__":
    main()