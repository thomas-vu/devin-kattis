def max_consecutive_hours(N, W, temperatures):
    max_attendance = 0
    
    for start in range(N):
        charge = W
        valid_sequence = True
        
        for i in range(start, N):
            required_charge = temperatures[i] / 30
            if charge < required_charge:
                valid_sequence = False
                break
            else:
                charge -= required_charge
        
        if valid_sequence:
            max_attendance = N - start
            break
    
    return max_attendance

# Read input
N, W = map(int, input().split())
temperatures = list(map(int, input().split()))

# Calculate and print the result
print(max_consecutive_hours(N, W, temperatures))