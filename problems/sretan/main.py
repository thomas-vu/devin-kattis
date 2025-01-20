def kth_lucky_number(k):
    lucky_numbers = []
    def generate_lucky_numbers(current, length):
        if length == 0:
            lucky_numbers.append(int(current))
            return
        generate_lucky_numbers(current + '4', length - 1)
        generate_lucky_numbers(current + '7', length - 1)
    
    for i in range(1, 10):
        generate_lucky_numbers('', i)
    
    lucky_numbers.sort()
    return str(lucky_numbers[k - 1])

# Read input
K = int(input().strip())

# Output the result
print(kth_lucky_number(K))