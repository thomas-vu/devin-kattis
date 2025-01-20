def calculate_efficiency(v, r):
    rate = r / 1000
    efficiency = v / rate
    return efficiency

def find_most_efficient_spacecar(n, d, cars):
    max_efficiency = -1
    best_racer = ""
    
    for car in cars:
        initials, velocity, fuel_consumed = car
        efficiency = calculate_efficiency(velocity, fuel_consumed)
        
        if efficiency > max_efficiency:
            max_efficiency = efficiency
            best_racer = initials
    
    return best_racer

# Read input
n = int(input())
d = float(input())
cars = [input().split() for _ in range(n)]

# Convert velocity and fuel_consumed to float
for i in range(n):
    cars[i][1] = float(cars[i][1])
    cars[i][2] = float(cars[i][2])

# Find and print the most efficient space-car
print(find_most_efficient_spacecar(n, d, cars))