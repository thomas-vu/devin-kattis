def find_multiples(numbers):
    first_number = numbers[0]
    multiples = set()
    for number in numbers:
        if first_number % number == 0:
            multiples.add(number)
    return sorted(multiples)

n = int(input())
numbers = [int(input()) for _ in range(n)]
multiples = find_multiples(numbers)
for multiple in multiples:
    print(multiple)