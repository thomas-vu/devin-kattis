def same_or_different(S, streets, T, properties):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    
    def intersect(l1, l2):
        d = (l1[0] - l1[2]) * (l2[1] - l2[3]) - (l1[1] - l1[3]) * (l2[0] - l2[2])
        if d == 0:
            return False
        ua = ((l2[0] - l2[2]) * (l1[1] - l1[3]) - (l2[1] - l2[3]) * (l1[0] - l1[2])) / d
        ub = ((l1[0] - l1[2]) * (l2[1] - l2[3]) - (l1[1] - l1[3]) * (l2[0] - l2[2])) / d
        return 0 <= ub <= 1 and 0 <= ua <= 1
    
    regions = {}
    for i in range(S):
        x1, y1, x2, y2 = streets[i]
        for j in range(i + 1, S):
            x3, y3, x4, y4 = streets[j]
            if intersect((x1, y1, x2, y2), (x3, y3, x4, y4)):
                regions[(i, j)] = True
    
    for i in range(T):
        p1, q1 = properties[i * 2]
        p2, q2 = properties[i * 2 + 1]
        region_p = set()
        region_q = set()
        for r in regions:
            if (p1, p2) in r or (p2, p1) in r:
                region_p.add(r[0] if (p1, p2) in r else r[2])
                region_q.add(r[1] if (p1, p2) in r else r[3])
        same = False
        for rp in region_p:
            if rp in region_q:
                same = True
                break
        print("same" if same else "different")

S = int(input())
streets = [tuple(map(int, input().split())) for _ in range(S)]
T = int(input())
properties = [tuple(map(int, input().split())) for _ in range(T * 2)]
same_or_different(S, streets, T, properties)