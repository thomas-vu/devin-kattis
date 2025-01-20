def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        clues = []
        for _ in range(n):
            clue = input().split()
            if clue[0] == 'greater':
                clues.append((int(clue[2]), True))
            elif clue[0] == 'less':
                clues.append((int(clue[2]), False))
            else:  # 'divisible'
                clues.append((int(clue[3]), True))
        
        min_val = 1
        max_val = 50000
        for clue in clues:
            if clue[1]:  # greater than
                min_val = max(min_val, clue[0] + 1)
            else:  # less than
                max_val = min(max_val, clue[0] - 1)
        
        if min_val > max_val:
            print("infinite")
        elif min_val == 1 and max_val == 50000:
            print("none")
        else:
            result = [str(i) for i in range(min_val, max_val + 1) if all(i % c[0] == 0 if c[1] else i < c[0] for c in clues)]
            if result:
                print(' '.join(result))
            else:
                print("none")

main()