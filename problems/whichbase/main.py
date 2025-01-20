def interpret_number(num_str, base):
    try:
        num = int(num_str, base)
        return num
    except ValueError:
        return 0

def main():
    P = int(input())
    for _ in range(P):
        K, num_str = input().split()
        K = int(K)
        
        octal_val = interpret_number(num_str, 8) if num_str[0] == '0' else 0
        decimal_val = int(num_str)
        hex_val = interpret_number(num_str, 16)
        
        print(f"{K} {octal_val} {decimal_val} {hex_val}")

if __name__ == "__main__":
    main()