def count_digit_preserving_pairs(A, B):
    def get_digits(num):
        return set(str(num))
    
    digit_preserving_pairs = []
    
    for x in range(A, B + 1):
        for y in range(x, B + 1):
            product = x * y
            digits_x = get_digits(x)
            digits_y = get_digits(y)
            combined_digits = get_digits(product)
            
            if digits_x.union(digits_y) == combined_digits:
                digit_preserving_pairs.append((x, y, product))
    
    return digit_preserving_pairs

def main():
    A, B = map(int, input().split())
    digit_preserving_pairs = count_digit_preserving_pairs(A, B)
    
    print(f"{len(digit_preserving_pairs)} digit-preserving pair(s)")
    for x, y, product in sorted(digit_preserving_pairs, key=lambda pair: (pair[0], pair[1])):
        print(f"x = {x}, y = {y}, xy = {product}")

if __name__ == "__main__":
    main()