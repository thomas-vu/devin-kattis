N = int(input())
E = int(input())
songs_known = set([1])  # Bard knows all songs initially

for _ in range(E):
    K, *villagers = map(int, input().split())
    if 1 in villagers:  # If the bard is present
        songs_known = set(villagers)
    else:  # If the bard is not present, villagers exchange songs
        songs_known &= set(villagers)

print("\n".join(sorted(songs_known)))