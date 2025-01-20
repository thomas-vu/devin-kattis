def count_digit_preserving_pairs(A, B):
    def get_digits(num):
        return sorted(str(num))
    
    digit_preserving_pairs = []
    
    for x in range(A, B + 1):
        for y in range(x, B + 1):
            product = x * y
            if get_digits(x) == get_digits(y) and get_digits(product) == get_digits(x) + get_digits(y):
                digit_preserving_pairs.append((x, y, product))
    
    return digit_preserving_pairs

def main():
    A, B = map(int, input().split())
    pairs = count_digit_preserving_pairs(A, B)
    
    print(f"{len(pairs)} digit-preserving pair(s)")
    for x, y, product in sorted(pairs, key=lambda pair: (pair[0], pair[1])):
        print(f"x = {x}, y = {y}, xy = {product}")

if __name__ == "__main__":
    main()