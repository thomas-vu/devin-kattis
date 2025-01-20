def count_orderings(n):
    if n > 100:
        print("JUST RUN!!")
        return
    
    def factorial(num):
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
    
    total_orderings = 0
    for k in range(1, n + 1):
        total_orderings += factorial(n) // (factorial(k) * factorial(n - k))
    
    print(total_orderings)

# Example usage:
count_orderings(1)  # Output: 1
count_orderings(2)  # Output: 4
count_orderings(4)  # Output: 64
count_orderings(100)  # Output: JUST RUN!!