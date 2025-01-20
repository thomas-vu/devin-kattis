def is_valid_isbn10(isbn):
    if len(isbn) != 10:
        return False
    s = sum((10 - i) * int(char) for i, char in enumerate(isbn[:-1]) if char.isdigit()) + int('X' == isbn[-1]) * 10
    return s % 11 == 0

def calculate_isbn13_checksum(isbn13):
    s = sum((3 if i % 2 else 1) * int(char) for i, char in enumerate(isbn13))
    return (10 - s % 10) % 10

def convert_isbn10_to_isbn13(isbn10):
    if not is_valid_isbn10(isbn10):
        return "invalid"
    isbn13 = f"978{isbn10[:-1]}"
    checksum = calculate_isbn13_checksum(isbn13)
    return f"{isbn13}{checksum}"

def main():
    T = int(input())
    for _ in range(T):
        isbn10 = input().replace("-", "")
        result = convert_isbn10_to_isbn13(isbn10)
        print(result)

if __name__ == "__main__":
    main()