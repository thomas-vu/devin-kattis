def main():
    n, k = map(int, input().split())
    preferences = [list(map(lambda x: x.strip(), input().split())) for _ in range(n)]
    player_count = int(input())
    players = [input().strip() for _ in range(player_count)]
    
    player_indices = {player: idx for idx, player in enumerate(players)}
    selected_players = [[] for _ in range(n)]
    
    taken_players = set()
    
    for _ in range(k):
        for i in range(n):
            current_preferences = preferences[i]
            for j, player in enumerate(current_preferences):
                if player not in taken_players:
                    selected_players[i].append(player)
                    taken_players.add(player)
                    break
    
    for team in selected_players:
        print(' '.join(team))

if __name__ == "__main__":
    main()