def min_moves_to_kill_hydra(heads, tails):
    if heads == 0 and tails % 2 == 1:
        return -1
    moves = 0
    while heads > 0 and tails > 0:
        if heads % 2 == 1:
            heads -= 1
            tails += 1
        else:
            half_heads = heads // 2
            if tails >= half_heads:
                tails -= half_heads
                heads -= 2 * half_heads
            else:
                tails += (half_heads - tails) // 2
                heads -= 2 * (half_heads - tails)
        moves += 1
    if heads == 0 and tails > 0:
        while tails > 0:
            if tails % 2 == 1:
                return -1
            tails -= 2
            moves += 1
    elif heads > 0:
        while heads > 0:
            if heads % 2 == 1:
                return -1
            heads -= 2
            moves += 1
    return moves

def main():
    while True:
        heads, tails = map(int, input().split())
        if heads == 0 and tails == 0:
            break
        result = min_moves_to_kill_hydra(heads, tails)
        print(result)

if __name__ == "__main__":
    main()