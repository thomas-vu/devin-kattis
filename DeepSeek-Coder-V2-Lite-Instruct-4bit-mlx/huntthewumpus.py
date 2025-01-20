import math

def generate_wumpus(seed):
    wumpuses = []
    for _ in range(4):
        seed = seed + math.floor(seed / 13) + 15
        wumpuses.append((seed % 10, seed // 10 % 10))
    return wumpuses

def manhattan_distance(point, wumpus):
    return abs(point[0] - wumpus[0]) + abs(point[1] - wumpus[1])

def main():
    seed = int(input())
    wumpuses = generate_wumpus(seed)
    guesses = [tuple(map(int, input().split())) for _ in range(int(input()))]
    
    captured_wumpuses = set()
    moves = 0

    for guess in guesses:
        if guess in captured_wumpuses:
            continue
        
        moves += 1
        wumpus_found = False
        for wumpus in wumpuses:
            if guess == wumpus:
                captured_wumpuses.add(guess)
                print("You hit a wumpus!")
                wumpus_found = True
                break
        
        if not wumpus_found:
            min_distance = float('inf')
            for wumpus in wumpuses:
                if wumpus not in captured_wumpuses:
                    distance = manhattan_distance(guess, wumpus)
                    min_distance = min(min_distance, distance)
            print(min_distance)
        
        if len(captured_wumpuses) == 4:
            break
    
    print("Your score is {} moves.".format(moves))

main()