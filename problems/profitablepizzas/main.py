def maximize_earnings(n, pizzas):
    # Sort the pizzas based on their deadline in ascending order
    pizzas.sort(key=lambda x: x[0])
    
    # Initialize the current time and the total money earned
    current_time = 0
    total_money = 0
    
    # Iterate through the sorted list of pizzas
    for deadline, money in pizzas:
        # If the current time plus one second is within the deadline
        if current_time + 1 <= deadline:
            # Deliver the pizza and update the total money earned
            current_time += 1
            total_money += money
    
    return total_money

# Read the number of pizzas to be delivered
n = int(input())
pizzas = []

# Read the pizzas' details and store them in a list
for _ in range(n):
    t_i, d_i = map(int, input().split())
    pizzas.append((t_i, d_i))

# Output the maximum amount of money you can get for delivering the pizzas
print(maximize_earnings(n, pizzas))