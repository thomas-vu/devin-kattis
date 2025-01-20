def convert_to_base27(s):
    mapping = {'B': '8', 'G': 'C', 'I': '1', 'O': '0', 'Q': '0', 'S': '5', 'U': 'V', 'Y': 'V', 'Z': '2'}
    new_s = ""
    for char in s:
        if char in mapping:
            new_s += mapping[char]
        else:
            new_s += char
    return new_s

def calculate_check_digit(base27_number):
    weights = [2, 4, 5, 7, 8, 10, 11, 13]
    sum_weighted = 0
    for i in range(8):
        digit = base27_number[i]
        if '0' <= digit <= '9':
            value = int(digit)
        else:
            value = ord(digit) - ord('A') + 10
        sum_weighted += weights[i] * value
    return (sum_weighted) % 27

def main():
    P = int(input())
    for _ in range(P):
        K, UCN = input().split()
        K = int(K)
        UCN_base27 = convert_to_base27(UCN)
        check_digit = calculate_check_digit(UCN_base27)
        expected_check_digit = int(UCN[-1]) if UCN[-1].isdigit() else ord(UCN[-1]) - ord('A') + 10
        if check_digit != expected_check_digit:
            print(f"{K} Invalid")
        else:
            base10_value = int(UCN_base27[:8], 27)
            print(f"{K} {base10_value}")

main()