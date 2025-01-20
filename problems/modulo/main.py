distinct_numbers = set()
for _ in range(10):
    number = int(input())
    distinct_numbers.add(number % 42)
print(len(distinct_numbers))