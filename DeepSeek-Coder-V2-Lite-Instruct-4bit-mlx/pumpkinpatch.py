def simulate_pumpkins(P, D, N, pumpkin_positions):
    for _ in range(D):
        next_positions = set()
        for r, c in pumpkin_positions:
            next_positions.add((r + 1, c))
            next_positions.add((r - 1, c))
            next_positions.add((r, c + 1))
            next_positions.add((r, c - 1))
        pumpkin_positions = next_positions
    
    alive_pumpkins = [0] * P
    for i, (r, c) in enumerate(pumpkin_positions):
        if (r, c) not in pumpkin_positions:
            alive_pumpkins[i] = D + 1
    
    return ["ALIVE" if day == 0 else day for day in alive_pumpkins]

def main():
    while True:
        try:
            P, D, N = map(int, input().split())
            pumpkin_positions = [tuple(map(int, input().split())) for _ in range(P)]
            result = simulate_pumpkins(P, D, N, pumpkin_positions)
            print(" ".join(result))
        except EOFError:
            break

if __name__ == "__main__":
    main()