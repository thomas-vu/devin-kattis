def calculate_ingredients(N):
    gin = 45 * N
    lemon_juice = 30 * N
    syrup = 10 * N
    lemon_slices = N
    return f"{gin} ml gin\n{lemon_juice} ml fresh lemon juice\n{syrup} ml simple syrup\n{lemon_slices} slice{'es' if N > 1 else ''} of lemon"

# Example usage:
print(calculate_ingredients(1))  # Output for 1 Gin Fizz
print(calculate_ingredients(2))  # Output for 2 Gin Fizzes