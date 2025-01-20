import math
h, v = map(int, input().split())
ladder_length = (h / math.sin(math.radians(v)))
print(math.ceil(ladder_length))