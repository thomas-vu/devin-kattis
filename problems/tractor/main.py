def count_reachable_points(A, B):
    points = set()
    max_steps = 32  # Maximum number of steps to ensure we cover all possibilities
    for x in range(max_steps):
        for y in range(max_steps):
            if (x == 0 and y == 0) or (x > A or y > B):
                continue
            distance = sum([2**i for i in range(x)]) + sum([2**i for i in range(y)])
            if distance <= A * 2 + B * 2:
                points.add((sum([2**i for i in range(x)]), sum([2**i for i in range(y)])))
    return len(points)

def main():
    N = int(input())
    results = []
    for _ in range(N):
        A, B = map(int, input().split())
        results.append(count_reachable_points(A, B))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()