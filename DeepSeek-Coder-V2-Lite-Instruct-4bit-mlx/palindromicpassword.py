def closest_palindrome(num):
    num_str = str(num)
    for i in range(100000, 1000000):
        if str(i) == str(i)[::-1]:
            if abs(num - i) < abs(num - num_str):
                return i
            elif abs(num - i) == abs(num - num_str) and i < num:
                return i
    return num

def main():
    N = int(input())
    numbers = [int(input()) for _ in range(N)]
    for number in numbers:
        print(closest_palindrome(number))

if __name__ == "__main__":
    main()