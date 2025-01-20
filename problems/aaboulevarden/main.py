# Assuming the input is provided in the following format:
# N
# bar1_beer
# bar2_beer
# ...
# barN_beer
# Q
# query1_barX_beerS
# query2_barX_beerS
# ...
# queryQ_barX_beerS

def find_nearest_bar(bars, beer_names, query):
    bar_index = query[0]
    target_beer = query[1]
    
    current_bar_beer = bars[bar_index]
    min_distance = float('inf')
    best_position = -1
    
    for i, beer in enumerate(beer_names):
        if beer == target_beer:
            distance = abs(bar_index - i)
            if distance < min_distance:
                min_distance = distance
                best_position = i
            elif distance == min_distance and abs(bar_index - i) < abs(best_position - bar_index):
                best_position = i
    
    return best_position - bar_index

# Read input
N = int(input())
bars = []
for _ in range(N):
    bars.append(input().strip())

Q = int(input())
queries = []
for _ in range(Q):
    query = input().strip().split()
    queries.append((int(query[0]), query[1]))

# Process queries
for query in queries:
    result = find_nearest_bar(bars, bars, query)
    print(result)