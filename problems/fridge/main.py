def find_smallest_missing(digits):
    digits = list(map(int, sorted(digits)))
    max_possible = int(''.join(map(str, digits))) + 1
    
    for i in range(1, max_possible):
        if str(i) not in digits:
            return i
    return max_possible

# Read input from standard input
digits = input().strip()
print(find_smallest_missing(digits))