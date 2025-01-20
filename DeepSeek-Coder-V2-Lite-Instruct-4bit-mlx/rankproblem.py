def update_rankings(teams, i, j):
    if i < j:
        return teams
    elif i > j:
        temp = teams[j-1]
        for k in range(j-1, i-1):
            teams[k] = teams[k+1]
        teams[i-1] = temp
    return teams

def main():
    n, m = map(int, input().split())
    teams = [f'T{i+1}' for i in range(n)]
    
    for _ in range(m):
        i, j = map(int, input().split())
        if i < j:
            continue
        else:
            teams = update_rankings(teams, i, j)
    
    print(' '.join(teams))

if __name__ == "__main__":
    main()