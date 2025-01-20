def max_velocity(N, stages):
    # Initialize the maximum velocity to 0
    max_v = 0
    
    # Iterate over all possible combinations of stages
    for mask in range(1, 1 << N):
        total_mass = 0
        net_force = 0
        
        # Calculate the total mass and net force for the current combination of stages
        for i in range(N):
            if mask & (1 << i):
                S, L, T, C = stages[i]
                total_mass += S + L
                net_force += T - (S + L) * 9.8
        
        # Check if the total mass is within the allowed limit
        if total_mass <= 10000:
            # Calculate the acceleration and velocity
            if net_force >= 0:
                acceleration = net_force / total_mass
                velocity = int(acceleration * 10)  # Integrate the acceleration over time
                max_v = max(max_v, velocity)
    
    return max_v

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()
index = 0

# Parse the number of test cases
def read_int():
    global index
    value = int(data[index])
    index += 1
    return value

# Parse the stages data
def read_stage():
    S = int(data[index])
    L = int(data[index + 1])
    T = int(data[index + 2])
    C = int(data[index + 3])
    index += 4
    return S, L, T, C

# Read the number of stages for each test case and the stages data
test_cases = []
while index < len(data):
    N = read_int()
    stages = [read_stage() for _ in range(N)]
    test_cases.append((N, stages))

# Solve each test case and output the result
for N, stages in test_cases:
    result = max_velocity(N, stages)
    print(result)