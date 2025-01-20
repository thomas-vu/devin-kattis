def find_leash_point(S, hatches):
    minX = S
    minY = S
    for x in range(S):
        for y in range(S):
            if (x, y) not in hatches:
                can_reach = True
                max_distance = 0
                for hx, hy in hatches:
                    distance = ((hx - x) ** 2 + (hy - y) ** 2) ** 0.5
                    if distance > max_distance:
                        max_distance = distance
                if max_distance <= (S / 2):
                    if x < minX or (x == minX and y < minY):
                        minX = x
                        minY = y
                else:
                    can_reach = False
    return (minX, minY) if can_reach else None

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    results = []
    
    for _ in range(N):
        S = int(data[index])
        H = int(data[index + 1])
        hatches = []
        for i in range(H):
            x = int(data[index + 2 + 2 * i])
            y = int(data[index + 3 + 2 * i])
            hatches.append((x, y))
        index += 3 + 2 * H
        
        leash_point = find_leash_point(S, hatches)
        if leash_point:
            results.append(f"{leash_point[0]} {leash_point[1]}")
        else:
            results.append("poodle")
    
    for result in results:
        print(result)

main()