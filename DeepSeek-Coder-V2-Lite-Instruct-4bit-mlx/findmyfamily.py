def find_potential_photos(k, photos):
    potential_photos = []
    for i in range(k):
        n = photos[i][0]
        heights = photos[i][1]
        for j in range(n):
            if heights[j] > heights[0]:  # Alice is on the left and taller than you
                for l in range(j+1, n):
                    if heights[l] > heights[j]:  # Bob is on the right and taller than Alice
                        potential_photos.append(i+1)  # Photo index is 1-based
                        break
                break
    return potential_photos

k = int(input())
photos = []
for _ in range(k):
    n = int(input())
    heights = list(map(int, input().split()))
    photos.append((n, heights))

potential_photos = find_potential_photos(k, photos)
print(len(potential_photos))
for photo in potential_photos:
    print(photo)