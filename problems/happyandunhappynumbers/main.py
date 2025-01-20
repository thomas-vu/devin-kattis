def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    return n == 1

def count_happy_numbers(A, B):
    count = 0
    for number in range(A, B + 1):
        if is_happy(number):
            count += 1
    return count

def main():
    T = int(input())
    results = []
    for _ in range(T):
        A, B = map(int, input().split())
        results.append(count_happy_numbers(A, B))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()