import math

def probability_of_hit(f, R, t, r, g):
    # Calculate the area of the ring
    ring_area = math.pi * (R**2 - (R - t)**2)
    
    # Calculate the area of one string
    string_area = 2 * math.pi * r * (R - t - f)
    
    # Calculate the area of a single gap between strings
    gap_area = g**2 * math.pi
    
    # Calculate the total area occupied by strings and gaps
    total_occupied_area = (math.ceil((2 * R) / (g + 2 * r))**2) * string_area + \
                           (math.ceil((2 * R) / (g + 2 * r)) - 1)**2 * gap_area
    
    # Calculate the effective area of the ring where the fly can land
    effective_area = ring_area - total_occupied_area
    
    # Calculate the probability of hitting the fly
    if effective_area <= 0:
        return 1.0
    
    fly_area = math.pi * f**2
    probability = effective_area / (ring_area + 1e-9)
    
    return probability

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    results = []
    
    for i in range(1, N + 1):
        f = float(data[i])
        R = float(data[i + N])
        t = float(data[i + 2 * N])
        r = float(data[i + 3 * N])
        g = float(data[i + 4 * N])
        
        P = probability_of_hit(f, R, t, r, g)
        results.append(f"Case #{i}: {P:.10f}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()