def luhn_checksum(number):
    digits = list(map(int, number))[::-1]
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] = sum(map(int, str(digits[i])))
    total_sum = sum(digits)
    return "PASS" if total_sum % 10 == 0 else "FAIL"

def main():
    T = int(input())
    for _ in range(T):
        number = input().strip()
        result = luhn_checksum(number)
        print(result)

if __name__ == "__main__":
    main()