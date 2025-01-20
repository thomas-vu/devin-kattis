def read_ints():
    return list(map(int, input().split()))

# Read the number of movies, horror list size, and similarities count
N, H, L = read_ints()
# Read the horror list of movies
horror_list = set(read_ints())

# Initialize a dictionary to store the Horror Index for each movie
horror_index = {i: float('inf') for i in range(N)}

# Read the similarities and update the Horror Index accordingly
for _ in range(L):
    a, b = read_ints()
    if a in horror_list:
        horror_index[b] = min(horror_index[b], 1)
    if b in horror_list:
        horror_index[a] = min(horror_index[a], 1)
    for similar in {a, b}:
        for other in horror_list:
            if similar != other and a not in horror_index[other]:
                continue
            horror_index[similar] = min(horror_index[similar], horror_index[other] + 1)

# Find the movie with the highest Horror Index, considering a tie by lowest ID
max_horror = -1
max_index = float('inf')
for movie, hi in horror_index.items():
    if hi != float('inf') and (hi > max_horror or (hi == max_horror and movie < max_index)):
        max_horror = hi
        max_index = movie

print(max_index)