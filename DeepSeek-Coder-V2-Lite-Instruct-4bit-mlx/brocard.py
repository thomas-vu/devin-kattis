import math

def angle_between_vectors(vx1, vy1, vx2, vy2):
    dot = vx1 * vx2 + vy1 * vy2
    det = vx1 * vy2 - vy1 * vx2
    angle = math.atan2(det, dot)
    return abs(angle)

def brocard_point(Ax, Ay, Bx, By, Cx, Cy):
    # Calculate vectors AB and AC
    ABx = Bx - Ax
    ABy = By - Ay
    ACx = Cx - Ax
    ACy = Cy - Ay
    
    # Calculate angles with respect to side AB and AC
    alpha = angle_between_vectors(ABx, ABy, Cx - Bx, Cy - By)
    beta = angle_between_vectors(ACx, ACy, Ax - Cx, Ay - Cy)
    gamma = angle_between_vectors(ABx, ABy, Ax - Bx, Ay - By)
    
    # Calculate Brocard point using the cotangent rule
    denominator = (alpha * ACx + beta * ABx) / (ACy * alpha - ABy * beta)
    x = (Cy * ACx - By * ABx) / denominator
    y = (Bx * ACy - Ax * ABx) / denominator
    
    return x, y

# Read number of test cases
P = int(input())
for _ in range(P):
    K, Ax, Ay, Bx, By, Cx, Cy = map(float, input().split())
    x, y = brocard_point(Ax, Ay, Bx, By, Cx, Cy)
    print(f"{int(K)} {x:.5f} {y:.5f}")