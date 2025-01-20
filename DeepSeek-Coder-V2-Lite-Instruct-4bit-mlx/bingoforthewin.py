import sys
from itertools import combinations

def calculate_probabilities(players, n, k):
    # Calculate the total number of unique numbers across all players' sheets
    all_numbers = set()
    for sheet in players:
        all_numbers.update(sheet)
    
    total_calls = len(all_numbers)
    
    # Calculate the probability for each player to finish last
    probabilities = []
    for i in range(n):
        # Calculate the number of unique numbers on each player's sheet
        player_numbers = set(players[i])
        unique_player_numbers = len(player_numbers)
        
        # Calculate the number of calls each player needs to make
        calls_needed = unique_player_numbers * k - sum(players[i])
        
        # Calculate the probability for this player to finish last
        if calls_needed >= total_calls:
            prob = 1.0
        else:
            # Calculate the number of remaining numbers after this player has finished
            remaining_numbers = total_calls - calls_needed
            prob = (remaining_numbers / len(all_numbers)) ** unique_player_numbers
        
        probabilities.append(prob)
    
    return probabilities

# Read input from stdin
n, k = map(int, sys.stdin.readline().split())
players = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Calculate probabilities
probabilities = calculate_probabilities(players, n, k)

# Output the probabilities
for prob in probabilities:
    print("{:.9f}".format(prob))