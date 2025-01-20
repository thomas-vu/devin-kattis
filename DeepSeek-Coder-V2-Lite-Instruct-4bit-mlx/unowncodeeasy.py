def find_secret_code(numbers):
    def is_valid_base(c, number):
        power = pow(number, c)
        return str(power).endswith(str(number))
    
    min_length = 10**4 + 1
    for number in numbers:
        min_length = min(min_length, len(str(number)))
    
    for c in range(2, min_length + 1):
        valid = True
        for number in numbers:
            if not is_valid_base(c, number):
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