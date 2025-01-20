def trailing_nonzero(n):
    if n == 0 or n == 1:
        return 1
    
    # Count the number of factors of 5 in n!
    count_factors_of_5 = 0
    for i in range(1, n + 1):
        num = i
        while num % 5 == 0:
            count_factors_of_5 += 1
            num //= 5
    
    # Compute n! / (2^count_factors_of_2 * 5^count_factors_of_5)
    result = 1
    for i in range(2, n + 1):
        num = i
        while num % 5 == 0:
            num //= 5
        while num % 2 == 0:
            count_factors_of_2 += 1
            num //= 2
        result = (result * num) % 10
    
    # Adjust for the number of factors of 2 removed by dividing by (2^count_factors_of_2 * 5^count_factors_of_5)
    for _ in range(count_factors_of_2 - count_factors_of_5):
        result = (result * 2) % 10
    
    return result

# Read input until a zero is encountered
while True:
    n = int(input())
    if n == 0:
        break
    print(trailing_nonzero(n))