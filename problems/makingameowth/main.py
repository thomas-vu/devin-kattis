N, P, X, Y = map(int, input().split())

# Calculate the time you spend reading
your_time = (P // N) * X

# Calculate the time your Meowth spends reading if they read at all
if P % N == 0:
    meowth_time = (P // N) * Y
else:
    meowth_time = ((P // N) + 1) * Y

# Total time spent reading together
total_time = your_time + meowth_time
print(total_time)