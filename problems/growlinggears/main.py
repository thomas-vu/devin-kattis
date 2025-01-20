def find_gear_with_max_torque(a, b, c):
    # The maximum torque for a given gear is at the vertex of the parabola
    # The RPM at the vertex is R = -b / (2 * a)
    # Therefore, the maximum torque T_max is:
    # T_max = -a * (-b / (2 * a))^2 + b * (-b / (2 * a)) + c
    # Simplifying, we get:
    # T_max = -a * (b^2 / (4 * a^2)) + b * (-b / (2 * a)) + c
    #       = -b^2 / (4 * a) - b^2 / (2 * a) + c
    #       = -3b^2 / (4 * a) + c
    R_max = -b / (2 * a)
    T_max = -a * R_max**2 + b * R_max + c
    return T_max, R_max

def solve(test_cases):
    results = []
    for gears in test_cases:
        max_torque = float('-inf')
        gear_with_max_torque = -1
        for i, (a, b, c) in enumerate(gears):
            torque, _ = find_gear_with_max_torque(a, b, c)
            if torque > max_torque:
                max_torque = torque
                gear_with_max_torque = i + 1
        results.append(gear_with_max_torque)
    return results

# Read input
import sys
input = sys.stdin.read
lines = input().split()

# Parse the number of test cases
num_test_cases = int(lines[0])
line_index = 1

# Process each test case
test_cases = []
for _ in range(num_test_cases):
    n = int(lines[line_index])
    line_index += 1
    gears = []
    for _ in range(n):
        a, b, c = map(int, lines[line_index].split())
        gears.append((a, b, c))
        line_index += 1
    test_cases.append(gears)

# Solve the problem and print the results
results = solve(test_cases)
for result in results:
    print(result)