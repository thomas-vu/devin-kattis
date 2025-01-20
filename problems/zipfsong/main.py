import sys
from collections import defaultdict

def zipfs_law(n):
    return n / (1 + i) if n > 0 else 0

# Read input
n, m = map(int, sys.stdin.readline().strip().split())
songs = []
for _ in range(n):
    f_i, s_i = sys.stdin.readline().strip().split()
    songs.append((int(f_i), s_i))

# Calculate Zipf's law predictions
total_plays = sum(f for f, _ in songs)
zipped_scores = defaultdict(float)
for i, (f_i, s_i) in enumerate(songs):
    zipped_scores[s_i] = f_i / zipfs_law(total_plays)

# Calculate song qualities and sort by quality and position in album
qualities = [(q_i, s_i) for s_i, q_i in zipped_scores.items()]
qualities.sort(key=lambda x: (-x[0], songs.index((int(zipped_scores[x[1]]), x[1]))))

# Output the top m songs
for q, s in qualities[:m]:
    print(s)