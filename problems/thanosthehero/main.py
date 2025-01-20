def min_lives_to_take(N, populations):
    # Sort the populations in descending order to check the preference rule
    sorted_populations = sorted(populations, reverse=True)
    
    # Check if the list is already perfect (sorted in descending order)
    if all(sorted_populations[i] > sorted_populations[i + 1] for i in range(N - 1)):
        return 0
    
    # If the list is not perfect, calculate the number of lives to take
    lives_to_take = 0
    for i in range(N - 1):
        if sorted_populations[i] <= sorted_populations[i + 1]:
            # Thanos has to take the life of at least one world
            lives_to_take += sorted_populations[i + 1] - sorted_populations[i] + 1
            # Adjust the population of the next world to maintain the preference rule
            sorted_populations[i + 1] = sorted_populations[i] - 1
    
    # Check if the list is perfect after adjustments
    if all(sorted_populations[i] > sorted_populations[i + 1] for i in range(N - 1)):
        return lives_to_take
    else:
        return 1

# Read input
N = int(input())
populations = list(map(int, input().split()))

# Output the result
print(min_lives_to_take(N, populations))