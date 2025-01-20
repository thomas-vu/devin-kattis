def min_time_to_cross(people):
    people.sort()
    n = len(people)
    total_time = 0
    while n > 3:
        # Send the two fastest and the slowest to cross, send the fastest back with the torch
        total_time += people[1] + people[0] + people[-1] + people[0]
        n -= 2
    if n == 3:
        total_time += people[0] + people[1] + people[2]
    elif n == 2:
        total_time += people[1]
    elif n == 1:
        total_time += people[0]
    
    return total_time, generate_strategy(people)

def generate_strategy(people):
    strategy = []
    people.sort()
    n = len(people)
    while n > 3:
        # Send the two fastest and the slowest to cross, send the fastest back with the torch
        strategy.append((people[1], people[0]))
        strategy.append((people[0]))
        strategy.append((people[-1], people[-2]))
        strategy.append((people[0]))
        n -= 2
    if n == 3:
        strategy.append((people[0], people[1]))
        strategy.append((people[0]))
        strategy.append((people[0], people[2]))
    elif n == 2:
        strategy.append((people[0], people[1]))
    elif n == 1:
        strategy.append((people[0]))
    
    return strategy

# Read input
n = int(input())
people = [int(input()) for _ in range(n)]

# Calculate and output the result
total_time, strategy = min_time_to_cross(people)
print(total_time)
for pair in strategy:
    if isinstance(pair, tuple):
        print(f"{pair[0]} {pair[1]}")
    else:
        print(pair)