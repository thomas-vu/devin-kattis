def main():
    rhyme = input().split()
    n = int(input())
    kids = [input().strip() for _ in range(n)]
    
    team1 = []
    team2 = []
    index = 0
    
    for word in rhyme:
        index = (index + len(word) - 1) % n
        if len(team1) <= len(team2):
            team1.append(kids[index])
        else:
            team2.append(kids[index])
    
    print(len(team1))
    for kid in team1:
        print(kid)
    print(len(team2))
    for kid in team2:
        print(kid)

if __name__ == "__main__":
    main()