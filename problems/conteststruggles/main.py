n, k = map(int, input().split())
d, s = map(int, input().split())

# Total sum of difficulties solved by Lotte's team
total_sum = k * s
# Remaining problems sum of difficulties
remaining_problems_sum = (n - k) * d

# If the total sum is greater than or equal to the remaining problems sum, it's possible
if total_sum <= remaining_problems_sum:
    # Calculate the average difficulty of the unsolved problems
    average_difficulty = (remaining_problems_sum - total_sum) / (n - k)
    print("{:.6f}".format(average_difficulty))
else:
    # If it's not possible, print "impossible"
    print("impossible")