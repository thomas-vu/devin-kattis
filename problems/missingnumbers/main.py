def find_missing_numbers(n, numbers):
    last_number = int(numbers[-1])
    missing_numbers = []
    
    for i in range(1, last_number + 1):
        if str(i) not in numbers:
            missing_numbers.append(i)
    
    if len(missing_numbers) == 0:
        print("good job")
    else:
        for number in missing_numbers:
            print(number)

n = int(input())
numbers = [input() for _ in range(n)]
find_missing_numbers(n, numbers)