from itertools import permutations

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def min_cost(N, M, bottles, couriers, restaurant):
    min_total_distance = float('inf')
    
    for order in permutations(range(N)):
        total_distance = 0
        current_position = restaurant
        
        for bottle_index in order:
            total_distance += manhattan_distance(current_position[0], current_position[1], bottles[bottle_index][0], bottles[bottle_index][1])
            current_position = bottles[bottle_index]
        
        total_distance += manhattan_distance(current_position[0], current_position[1], restaurant[0], restaurant[1])
        
        min_total_distance = min(min_total_distance, total_distance)
    
    return min_total_distance

# Read input
N, M = map(int, input().split())
bottles = [tuple(map(int, input().split())) for _ in range(N)]
couriers = [tuple(map(int, input().split())) for _ in range(M)]
restaurant = tuple(map(int, input().split()))

# Calculate and print the minimum cost
print(min_cost(N, M, bottles, couriers, restaurant))