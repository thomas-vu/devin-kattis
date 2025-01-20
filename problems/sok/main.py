# Solution to the problem
A, B, C = map(int, input().split())
I, J, K = map(int, input().split())

# Calculate the number of cocktails that can be made
cocktails = min(A / I, B / J, C / K)

# Calculate the leftover amount for each juice
leftover_orange = A - cocktails * I
leftover_apple = B - cocktails * J
leftover_pineapple = C - cocktails * K

# Print the result with 6 decimal places
print("{:.6f} {:.6f} {:.6f}".format(leftover_orange, leftover_apple, leftover_pineapple))