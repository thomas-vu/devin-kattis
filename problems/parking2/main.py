def min_walking_distance(positions):
    positions.sort()
    median = positions[len(positions) // 2]
    return sum(abs(pos - median) for pos in positions)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        positions = list(map(int, input().split()))
        print(min_walking_distance(positions))

if __name__ == "__main__":
    main()