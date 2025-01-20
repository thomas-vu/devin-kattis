def mean_temperature(M, readings):
    total = sum(readings)
    mean = total // M
    return mean

# Read input
M = int(input())
readings = list(map(int, input().split()))

# Calculate and print the mean temperature
mean_temp = mean_temperature(M, readings)
print(mean_temp)