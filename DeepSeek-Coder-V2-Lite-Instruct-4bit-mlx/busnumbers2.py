def find_bus_numbers(m):
    cubes = {}
    for a in range(1, int(m**(1/3)) + 1):
        for b in range(a, int(m**(1/3)) + 1):
            sum_cubes = a**3 + b**3
            if sum_cubes > m:
                break
            if sum_cubes not in cubes:
                cubes[sum_cubes] = 1
            else:
                cubes[sum_cubes] += 1
    
    bus_numbers = [num for num, count in cubes.items() if count >= 2]
    bus_numbers.sort()
    
    for num in reversed(bus_numbers):
        if num <= m:
            return num
    return "none"

# Read input from stdin
m = int(input().strip())
result = find_bus_numbers(m)
print(result)