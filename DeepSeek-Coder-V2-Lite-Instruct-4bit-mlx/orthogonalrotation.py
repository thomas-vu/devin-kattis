n = int(input())
v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))

def is_orthogonal(vec1, vec2):
    return sum(a * b for a, b in zip(vec1, vec2)) == 0

rotations = []
for k in range(n):
    rotated_v2 = v2[k:] + v2[:k]
    if is_orthogonal(v1, rotated_v2):
        rotations.append(k)

if rotations:
    for rotation in rotations:
        print(rotation)
else:
    print(-1)