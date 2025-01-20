def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify(p, q):
    g = gcd(abs(p), abs(q))
    p //= g
    q //= g
    return (p, q)

def wheel_movement(x1, y1, r1, x2, y2, r2):
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    if d == r1 + r2:
        return (1, 0)
    elif d < r1 - r2 or d > r1 + r2:
        return (0, 1)
    else:
        a = (r1**2 - r2**2 + d**2) / (2 * d)
        h = (r1**2 - a**2)**0.5
        theta1 = atan2(y2 - y1, x2 - x1)
        theta2 = atan2(x1 - x2, y1 - y2)
        omega1 = 1
        omega2 = (r1**2 - r2**2 + d**2) / (d * r2)
        omega2 = -omega2 if theta1 > theta2 else omega2
        return simplify(int(round(omega2)), int(round(r2)))

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        index += 1
        wheels = []
        for _ in range(n):
            x, y, r = int(data[index]), int(data[index+1]), int(data[index+2])
            wheels.append((x, y, r))
            index += 3
        
        outputs = []
        for i in range(n):
            if i == 0:
                outputs.append("1 clockwise")
            else:
                x1, y1, r1 = wheels[0]
                x2, y2, r2 = wheels[i]
                p, q = wheel_movement(x1, y1, r1, x2, y2, r2)
                if p == 0:
                    outputs.append("not moving")
                else:
                    if q == 1:
                        outputs.append(f"{p}")
                    else:
                        outputs.append(f"{p}/{q}")
        results.append("\n".join(outputs))
    
    print("\n\n".join(results))

if __name__ == "__main__":
    main()