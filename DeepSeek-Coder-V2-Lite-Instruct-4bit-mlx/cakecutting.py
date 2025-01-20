def count_pieces(N, cuts):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    
    def inside(p, polygon):
        n = len(polygon)
        if sign(p, polygon[0], polygon[1]) < 0:
            return False
        if sign(p, polygon[-1], polygon[0]) > 0:
            return False
        i = 1
        j = n - 1
        while i < j:
            h = (i + j) // 2
            if sign(p, polygon[h], polygon[0]) < 0:
                j = h
            else:
                i = h
        return sign(p, polygon[i], polygon[0]) > 0
    
    cuts_set = set()
    for x1, y1, x2, y2 in cuts:
        if (x1, y1) not in cuts_set and (x2, y2) not in cuts_set:
            cuts_set.add((x1, y1))
    
    polygon = []
    for x, y in cuts_set:
        polygon.append((x, y))
    
    n = len(polygon)
    if n <= 2:
        return n
    
    points = list(polygon) + [polygon[0]]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            pi = points[i]
            pj = points[j]
            intersect_count = 0
            for k in range(n):
                pk = points[k]
                p_next = points[k + 1]
                if (pi[0] - pj[0]) * (pk[1] - pi[1]) + (pj[1] - pi[1]) * (pk[0] - pj[0]) == 0 and
                    min(pi[0], pj[0]) <= pk[0] <= max(pi[0], pj[0]) and
                    min(pi[1], pj[1]) <= pk[1] <= max(pi[1], pj[1])):
                    intersect_count += 1
                elif (pi[0] - pj[0]) * (pk[1] - pi[1]) + (pj[1] - pi[1]) * (pk[0] - pj[0]) == 0 and
                      min(pi[0], pj[0]) <= pk[0] <= max(pi[0], pj[0]) and
                      min(pi[1], pj[1]) <= pk[1] <= max(pi[1], pj[1])):
                    intersect_count += 1
                elif (pi[0] - pj[0]) * (pk[1] - pi[1]) + (pj[1] - pi[1]) * (pk[0] - pj[0]) == 0 and
                      min(pi[0], pj[0]) <= pk[0] <= max(pi[0], pj[0]) and
                      min(pi[1], pj[1]) <= pk[1] <= max(pi[1], pj[1])):
                    intersect_count += 1
            count += intersect_count // 2
    return count + 1

N = int(input())
cuts = [tuple(map(int, input().split())) for _ in range(N)]
print(count_pieces(N, cuts))