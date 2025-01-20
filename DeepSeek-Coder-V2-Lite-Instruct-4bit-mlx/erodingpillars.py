import math

def min_jump_distance(pillars):
    # Calculate the minimum jump distance needed to reach any pillar and return to start
    min_distance = float('inf')
    for i in range(len(pillars)):
        for j in range(i + 1, len(pillars)):
            dist = math.sqrt((pillars[i][0] - pillars[j][0])**2 + (pillars[i][1] - pillars[j][1])**2)
            min_distance = min(min_distance, dist / 2)
    return min_distance

def main():
    n = int(input())
    pillars = [tuple(map(int, input().split())) for _ in range(n)]
    result = min_jump_distance(pillars)
    print("{:.15f}".format(result))

if __name__ == "__main__":
    main()