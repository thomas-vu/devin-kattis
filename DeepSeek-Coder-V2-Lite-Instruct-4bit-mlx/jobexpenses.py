N = int(input())
numbers = list(map(int, input().split()))
total_expenses = sum(-num for num in numbers if num < 0)
print(total_expenses)