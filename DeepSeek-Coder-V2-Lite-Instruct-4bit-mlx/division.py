def is_integer_with_less_than_100_digits(numerator, denominator):
    result = numerator // denominator
    return len(str(result)) < 100

def main():
    while True:
        try:
            t, a, b = map(int, input().split())
            if t**a - 1 == 0 or t**b - 1 == 0:
                print(f"({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits.")
            else:
                numerator = t**a - 1
                denominator = t**b - 1
                if is_integer_with_less_than_100_digits(numerator, denominator):
                    print(f"({t}^{a}-1)/({t}^{b}-1) {numerator // denominator}")
                else:
                    print(f"({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits.")
        except EOFError:
            break

if __name__ == "__main__":
    main()