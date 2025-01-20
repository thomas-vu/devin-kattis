def main():
    N = int(input())
    teams = []
    for _ in range(N):
        university, team_name = input().split()
        teams.append((university, team_name))
    
    unique_universities = set()
    winners = []
    
    for team in sorted(teams, key=lambda x: (x[0], x[1])):
        if team[0] not in unique_universities:
            winners.append(team)
            unique_universities.add(team[0])
        if len(winners) == 12:
            break
    
    for winner in winners:
        print(winner[0], winner[1])

if __name__ == "__main__":
    main()