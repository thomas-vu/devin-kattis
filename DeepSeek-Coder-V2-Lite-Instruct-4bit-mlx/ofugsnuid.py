n = int(input())
numbers = [int(input()) for _ in range(n)]
for number in reversed(numbers):
    print(number)