def min_moves(s1, s2):
    moves = 0
    n = len(s1)
    
    for i in range(n):
        diff = ord(s2[i]) - ord(s1[i])
        if diff == 0:
            continue
        elif diff > 0:
            shift_count = min(diff, 26 - diff)
        else:
            shift_count = min(-diff, 26 + diff)
        
        moves += shift_count
    
    return moves

def main():
    while True:
        try:
            s1, s2 = input().split()
            result = min_moves(s1, s2)
            print(result)
        except EOFError:
            break

if __name__ == "__main__":
    main()