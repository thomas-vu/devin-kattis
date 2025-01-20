def find_consecutive_sum(N):
    # Start with the smallest possible number of summands, which is 2 (since we need at least two numbers)
    k = 2
    
    while True:
        # Calculate the sum of k consecutive integers starting from x
        x = (N - (k * (k - 1) // 2)) / k
        
        if x <= 0:
            # If x is not a positive integer, then it's impossible to find such summands
            return "IMPOSSIBLE"
        else:
            x = int(x)  # Convert to integer since the problem specifies positive integers
            
            if x > 0:
                # If we found a valid sequence of consecutive integers, return the equation
                summands = [str(x + i) for i in range(k)]
                return f"{N} = {' + '.join(summands)}"
        
        k += 1

# Read the number of test cases
T = int(input())

for _ in range(T):
    N = int(input())
    result = find_consecutive_sum(N)
    print(result)