def is_winnable(rooms, start, finish):
    energy = [0] * (len(rooms) + 1)
    energy[start] = 100
    
    for i in range(len(rooms)):
        e = rooms[i][0]
        for door in rooms[i][1:]:
            if energy[door] < energy[i] + e:
                energy[door] = energy[i] + e
        if energy[finish] > 0:
            return "winnable"
    return "hopeless"

while True:
    n = int(input())
    if n == -1:
        break
    
    rooms = []
    for _ in range(n):
        room_info = list(map(int, input().split()))
        rooms.append(room_info)
    
    start = 0
    finish = n - 1
    result = is_winnable(rooms, start, finish)
    print(result)