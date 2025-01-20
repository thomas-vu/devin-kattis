def find_max_speed(n, photos):
    max_speed = 0
    for i in range(1, n):
        time_diff = photos[i][0] - photos[i-1][0]
        dist_diff = photos[i][1] - photos[i-1][1]
        speed = dist_diff / time_diff
        max_speed = max(max_speed, int(speed))
    return max_speed

n = int(input())
photos = [tuple(map(int, input().split())) for _ in range(n)]
print(find_max_speed(n, photos))