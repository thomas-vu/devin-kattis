import math

def largest_pie_size(radii, F):
    low, high = 0.0, max(radii) ** 2 * math.pi
    
    while high - low > 1e-6:
        mid = (low + high) / 2.0
        count = sum([math.pi * r**2 / mid for r in radii])
        
        if count >= F + 1:  # Including myself
            low = mid
        else:
            high = mid
    
    return low

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        N, F = map(int, input().split())
        radii = list(map(int, input().split()))
        result = largest_pie_size(radii, F)
        results.append("{:.8f}".format(result))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()