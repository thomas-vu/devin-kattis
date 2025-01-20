def max_safe_operations(registers):
    # Define the primes for each register
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    
    # Calculate the maximum safe number of operations for each register
    max_ops = []
    for i in range(8):
        if registers[i] < primes[i] - 1:
            max_ops.append(primes[i] - registers[i])
        else:
            max_ops.append(0)
    
    # Find the minimum of these values, which determines the maximum safe number of operations
    min_ops = min(max_ops)
    
    # Calculate the total number of additional operations by multiplying the min_ops with each register's max capacity
    total_operations = 1
    for i in range(8):
        if max_ops[i] != 0:
            total_operations *= max_ops[i]
    
    return total_operations

# Read input from stdin
registers = list(map(int, input().split()))

# Calculate and print the result
print(max_safe_operations(registers))