import math

def calculate_landing(H, L, j, p):
    g = 9.81
    
    # Determine the height at the end of the ski jump approach
    h_end = 2 * H * (1 - (L / (2 * L)) ** 2)
    
    # Determine the position where the height is less than or equal to h_end
    l = L / 2 + (H - h_end) * (L / H) ** 0.5
    
    # Determine the speed at landing using energy conservation
    v_l = math.sqrt(-2 * g * (H + p - h_end))
    
    # Determine the angle using vector analysis
    vx = v_l * (L / 2) / math.sqrt((L / 2) ** 2 + (H - h_end) ** 2)
    vy = math.sqrt(v_l ** 2 - vx ** 2)
    alpha = math.degrees(math.atan2(vy, vx))
    
    return l, v_l, alpha

def main():
    t = int(input())
    results = []
    
    for _ in range(t):
        j, p, H, L = map(int, input().split())
        l, v_l, alpha = calculate_landing(H, L, j, p)
        results.append((l, v_l, alpha))
    
    for result in results:
        print("{:.8f} {:.8f} {:.8f}".format(*result))

if __name__ == "__main__":
    main()