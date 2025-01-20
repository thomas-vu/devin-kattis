def can_reach_gas_station(C, X, M, fuel_efficiencies):
    # Calculate the minimum time to reach the gas station without considering the leak
    min_time = M / max(fuel_efficiencies)
    
    # Calculate the fuel loss in the time it takes to reach the gas station
    max_fuel_needed = min_time * X
    
    # Check if the driver can reach the gas station with the remaining fuel after the leak
    if C - max_fuel_needed >= 0:
        return True, max(fuel_efficiencies)
    else:
        return False, 0

# Read input
C = float(input().split()[0])
X = float(input().split()[1])
M = float(input().split()[2])
fuel_efficiencies = [float(input().split()[-1]) for _ in range(6)]

# Check if the driver can reach the gas station
reachable, max_speed = can_reach_gas_station(C, X, M, fuel_efficiencies)

# Output the result
if reachable:
    print("YES", max_speed)
else:
    print("NO")