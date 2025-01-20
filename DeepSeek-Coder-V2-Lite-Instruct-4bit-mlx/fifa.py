# Read the input from stdin
n = int(input())
k = int(input())

# Calculate the current year based on the number of improvements and the frequency of improvements
current_year = 2022 + (n // k)

# Print the current year
print(current_year)