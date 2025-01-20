def max_health_boost(green, red):
    # Calculate the maximum health boost by considering all possible combinations
    if green == 0:
        return red * 10  # Only red herbs can be eaten
    if green == 1:
        return max(red * 10 + 3, red * 10)  # Eat one green herb or eat all red herbs
    if green == 2:
        return max(red * 10 + 3, red * 10 + 10)  # Eat two green herbs or eat all red herbs
    if green >= 3:
        return max(red * 10 + 10, red * 10 + (green - 3) * 10 + 3)
        # Eat three green herbs or eat one red herb and the rest of the green herbs optimally
    return 0

# Read input from stdin
green, red = map(int, input().split())

# Output the result
print(max_health_boost(green, red))