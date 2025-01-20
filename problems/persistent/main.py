def persistence(n):
    count = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        count += 1
    return count if n < 10 else -1

def find_smallest_number():
    while True:
        n = int(input())
        if n == -1:
            break
        result = find_smallest(n)
        if result == -1:
            print("There is no such number.")
        else:
            print(result)

def find_smallest(target):
    for i in range(1, 10**4):  # A reasonable upper bound to find the smallest number
        if persistence(i) == target:
            return i
    return -1

find_smallest_number()