import math

def calculate_distance(R, h1, h2):
    # Convert heights from meters to kilometers
    h1 = h1 / 1000
    h2 = h2 / 1000
    
    # Calculate the distance between the observer and the lighthouse
    D = math.sqrt((R + h1)**2 - (R + h2)**2)
    
    return D

def main():
    t = int(input())
    results = []
    
    for _ in range(t):
        R, h1, h2 = map(float, input().split())
        D = calculate_distance(R, h1, h2)
        results.append(D)
    
    for result in results:
        print("{:.10f}".format(result))

if __name__ == "__main__":
    main()