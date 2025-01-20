import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def main():
    # Read input
    Bx, Cx, Cy = map(float, input().split())
    
    # Calculate coordinates of points B and C
    B = (Bx, 0)
    C = (Cx, Cy)
    
    # Calculate radius of the circumscribed circle O
    a = distance((0, 0), B)
    b = distance((0, 0), C)
    c = distance(B, C)
    s = (a + b + c) / 2
    R = (a * b * c) / (4 * math.sqrt(s * (s - a) * (s - b) * (s - c)))
    
    # Calculate the incenter I
    Ax = 0
    Ay = 0
    Bx, By = B
    Cx, Cy = C
    
    # Calculate the circumcenter O
    D = Bx**2 + By**2
    E = Cx**2 + Cy**2
    F = Bx*Cx + By*Cy
    Gx = (By*(E - D) - Cy*F) / 2
    Gy = (-(Bx*(E - D)) + Cx*F) / 2
    O = (Gx, Gy)
    
    # Calculate the second points of intersection of the lines through A and I, B and I resp. C and I with the circle O
    Kx = (Ay*(O[0]**2 + O[1]**2 - R**2) - 2*O[0]*R*Ay + Ax*(Ax*O[0] - O[1]**2)) / (2*Ax*O[0] - 2*Ay*O[1])
    Ky = (Ax*(O[0]**2 + O[1]**2 - R**2) - 2*O[1]*R*Ax + Ay*(Ay*O[1] - O[0]**2)) / (2*Ay*O[1] - 2*Ax*O[0])
    M = (Kx, Ky)
    
    # Calculate the lengths of the segments EF, FG, GH, HJ, JK and KE
    E = (0, 0)
    F = (0, 0)
    G = (0, 0)
    H = (0, 0)
    J = (0, 0)
    K = (0, 0)
    
    EF = distance(E, F)
    FG = distance(F, G)
    GH = distance(G, H)
    HJ = distance(H, J)
    JK = distance(J, K)
    KE = distance(K, E)
    
    # Print the results
    print("{:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f}".format(EF, FG, GH, HJ, JK, KE))

if __name__ == "__main__":
    main()