def calculate_expected_profit(x, p):
    # Calculate the expected profit given x and p
    win_probability = p / 100
    loss_probability = 1 - win_probability
    expected_profit = (win_probability * 2) - loss_probability * 2 + (loss_probability * ((100 - x) / 100))
    return expected_profit

# Read input from stdin
x, p = map(float, input().split())

# Calculate the maximum expected profit
max_expected_profit = calculate_expected_profit(x, p)

# Print the result with an absolute error of at most 10^-3
print("{:.3f}".format(max_expected_profit))