import math

def main():
    N = int(input())
    people = [tuple(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    transmitters = [int(input()) for _ in range(Q)]
    
    results = []
    
    for d in transmitters:
        count = 0
        for x, y in people:
            if math.sqrt(x**2 + y**2) <= d:
                count += 1
        results.append(count)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()