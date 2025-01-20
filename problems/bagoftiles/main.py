def calculate_odds(tiles, n, t):
    from itertools import combinations
    
    winning_outcomes = 0
    total_outcomes = 0
    
    for draw in combinations(tiles, n):
        total_outcomes += 1
        if sum(draw) == t:
            winning_outcomes += 1
    
    return f"{winning_outcomes}:{total_outcomes - winning_outcomes}"

def main():
    g = int(input())
    for _ in range(g):
        m = int(input())
        tiles = list(map(int, input().split()))
        n, t = map(int, input().split())
        print(f"Game {_+1} -- {calculate_odds(tiles, n, t)}")

if __name__ == "__main__":
    main()