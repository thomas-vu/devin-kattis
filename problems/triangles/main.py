def is_tangled(tri1, tri2):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    
    def point_inside_triangle(pt, tri):
        d1 = sign(pt, tri[0], tri[1])
        d2 = sign(pt, tri[1], tri[2])
        d3 = sign(pt, tri[2], tri[0])
        
        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
        
        return not (has_neg and has_pos)
    
    def triangles_intersect(tri1, tri2):
        for i in range(3):
            for j in range(3):
                if point_inside_triangle(tri1[i], tri2) or point_inside_triangle(tri2[j], tri1):
                    return True
        return False
    
    if triangles_intersect(tri1, tri2):
        return "YES"
    else:
        return "NO"

T = int(input())
for _ in range(T):
    tri1 = [list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))]
    tri2 = [list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))]
    print(is_tangled(tri1, tri2))