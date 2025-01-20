def find_minimum_setlist(M, S):
    preferences = []
    for _ in range(M):
        prefs = list(map(int, input().split()))
        preferences.append(prefs)
    
    song_prefers = {song: set() for song in range(1, S+1)}
    
    for prefs in preferences:
        for i in range(len(prefs)):
            for j in range(i+1, len(prefs)):
                song_prefers[prefs[j]].add(prefs[i])
    
    min_setlist = set()
    for song in range(1, S+1):
        if all(song in song_prefers[better_song] for better_song in song_prefers if song < better_song):
            min_setlist.add(song)
    
    sorted_min_setlist = sorted(list(min_setlist))
    print(len(sorted_min_setlist))
    print(' '.join(map(str, sorted_min_setlist)))

# Read input from stdin
M, S = map(int, input().split())
find_minimum_setlist(M, S)