import sys
from itertools import permutations

def read_input():
    n = int(sys.stdin.readline().strip())
    runners = []
    for _ in range(n):
        name, a, b = sys.stdin.readline().strip().split()
        runners.append((name, float(a), float(b)))
    return n, runners

def calculate_team_time(runners):
    min_time = float('inf')
    best_team = None
    
    for perm in permutations(runners, 4):
        total_time = perm[0][1] + perm[1][2] + perm[2][2] + perm[3][2]
        if total_time < min_time:
            min_time = total_time
            best_team = perm
    
    return min_time, best_team

def main():
    n, runners = read_input()
    min_time, best_team = calculate_team_time(runners)
    
    print("{:.6f}".format(min_time))
    for runner in best_team:
        print(runner[0])

if __name__ == "__main__":
    main()