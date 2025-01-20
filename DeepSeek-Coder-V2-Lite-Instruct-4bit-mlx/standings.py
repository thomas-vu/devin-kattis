def calculate_badness(teams):
    teams.sort(key=lambda x: x[1])  # Sort by preferred place
    total_badness = 0
    for i, (_, pref) in enumerate(teams):
        total_badness += abs(i + 1 - pref)
    return total_badness

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        index += 1  # Skip the blank line
        N = int(data[index])
        index += 1
        teams = []
        for _ in range(N):
            team_name = data[index]
            preferred_place = int(data[index + 1])
            teams.append((team_name, preferred_place))
            index += 2
        badness = calculate_badness(teams)
        results.append(badness)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()