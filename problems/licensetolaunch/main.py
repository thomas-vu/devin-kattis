n = int(input())
junk_counts = list(map(int, input().split()))

# Find the day with the minimum space junk
min_junk = min(junk_counts)
# Find all days with the minimum space junk
min_days = [i for i, count in enumerate(junk_counts) if count == min_junk]
# The day to launch is the first of these minimum days
launch_day = min_days[0]

# Output the number of days to wait before launching
print(launch_day)