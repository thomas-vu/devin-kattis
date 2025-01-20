def stable_sort(attributes, songs):
    for _ in range(int(input())):
        attr = input()
        songs.sort(key=lambda x: (x[attr]))
        print(' '.join(attributes))
        for song in songs:
            print(' '.join([song[a] for a in attributes]))
        print()

attributes = input().split()
songs = []
for _ in range(int(input())):
    songs.append(dict(zip(attributes, input().split())))
stable_sort(attributes, songs)