pieces = list(map(int, input().split()))
while pieces != [1, 2, 3, 4, 5]:
    if pieces[0] > pieces[1]:
        pieces[0], pieces[1] = pieces[1], pieces[0]
    if pieces[1] > pieces[2]:
        pieces[1], pieces[2] = pieces[2], pieces[1]
    if pieces[2] > pieces[3]:
        pieces[2], pieces[3] = pieces[3], pieces[2]
    if pieces[3] > pieces[4]:
        pieces[3], pieces[4] = pieces[4], pieces[3]
    print(' '.join(map(str, pieces)))