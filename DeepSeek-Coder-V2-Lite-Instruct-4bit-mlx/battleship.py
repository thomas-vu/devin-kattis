def count_ships(maps):
    ships = 0
    for row in maps:
        ships += row.count('#')
    return ships

def simulate_game(width, height, player1_map, player2_map, shots):
    hits1 = [[False] * width for _ in range(height)]
    hits2 = [[False] * width for _ in range(height)]
    
    for shot in shots:
        x, y = shot
        if player1_map[y][x] == '#' and not hits1[y][x]:
            hits1[y][x] = True
        elif player2_map[y][x] == '#' and not hits2[y][x]:
            hits2[y][x] = True
    
    ships1 = count_ships([['#' if hits1[i][j] else '_' for j in range(width)] for i in range(height)])
    ships2 = count_ships([['#' if hits2[i][j] else '_' for j in range(width)] for i in range(height)])
    
    if ships1 == 0 and ships2 == 0:
        return "draw"
    elif ships1 == 0:
        return "player two wins"
    elif ships2 == 0:
        return "player one wins"
    else:
        return None

def main():
    t = int(input())
    results = []
    
    for _ in range(t):
        w, h, n = map(int, input().split())
        player1_map = [input() for _ in range(h)]
        player2_map = [input() for _ in range(h)]
        shots = [tuple(map(int, input().split())) for _ in range(n)]
        
        result = simulate_game(w, h, player1_map, player2_map, shots)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()