def is_consistent(phone_numbers):
    phone_numbers.sort()
    for i in range(len(phone_numbers) - 1):
        if phone_numbers[i] == phone_numbers[i + 1][:len(phone_numbers[i])]:
            return "NO"
    return "YES"

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        phone_numbers = [input().strip() for _ in range(n)]
        result = is_consistent(phone_numbers)
        print(result)

if __name__ == "__main__":
    main()