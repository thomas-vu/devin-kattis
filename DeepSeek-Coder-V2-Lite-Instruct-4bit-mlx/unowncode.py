def find_secret_code(numbers):
    def is_valid(c, number):
        power = pow(number, c)
        return str(power).endswith(str(number))
    
    min_length = float('inf')
    for number in numbers:
        length = len(str(number))
        min_length = min(min_length, length)
    
    for c in range(2, 10**5):
        valid = True
        for number in numbers:
            if not is_valid(c, number):
                valid = False
                break
        if valid:
            return c
    return -1

# Read input
N = int(input())
numbers = list(map(int, input().split()))

# Output the result
print(find_secret_code(numbers))