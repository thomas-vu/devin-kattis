n, V = map(int, input().split())
boxes = [tuple(map(int, input().split())) for _ in range(n)]

largest_box = max(boxes, key=lambda box: box[0] * box[1] * box[2])
largest_volume = largest_box[0] * largest_box[1] * largest_box[2]
difference = largest_volume - V

print(difference)