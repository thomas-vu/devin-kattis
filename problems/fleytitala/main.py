d, k = int(input()), int(input())
total_distance = d * (1 - 0.5**(k + 1)) / (1 - 0.5)
print("{:.9f}".format(total_distance))