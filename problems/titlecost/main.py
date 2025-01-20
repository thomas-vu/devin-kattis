def calculate_cost(movie_title, cost_cap):
    title_length = len(movie_title)
    return min(title_length, cost_cap)

# Read input from stdin
input_line = input().strip()
movie_title, cost_cap = input_line.split()
cost_cap = float(cost_cap)

# Calculate and output the result
result = calculate_cost(movie_title, cost_cap)
print("{:.2f}".format(result))