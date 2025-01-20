import sys

def min_distance(n, vehicles):
    leftmost = float('inf')
    rightmost = -float('inf')
    
    for x, v in vehicles:
        leftmost = min(leftmost, x + v)
        rightmost = max(rightmost, x - v)
    
    return (leftmost - rightmost) / 2.0

def main():
    n = int(sys.stdin.readline().strip())
    vehicles = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    result = min_distance(n, vehicles)
    print("{:.10f}".format(result))

if __name__ == "__main__":
    main()