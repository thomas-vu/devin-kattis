def main():
    n, k, c = map(int, input().split())
    teams = [list(map(int, input().split())) for _ in range(n)]
    
    school_count = {}
    for team in teams:
        t, s = team
        school_count[s] = school_count.get(s, 0) + 1
    
    qualified = []
    for team in teams:
        t, s = team
        if school_count[s] <= c:
            qualified.append(t)
            school_count[s] += 1
    
    for team in sorted(qualified):
        print(team)

if __name__ == "__main__":
    main()