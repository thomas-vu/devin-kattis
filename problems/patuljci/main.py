def find_dwarves():
    hats = [int(input()) for _ in range(9)]
    total_sum = sum(hats)
    
    for i in range(8):
        for j in range(i + 1, 9):
            if total_sum - hats[i] - hats[j] == 100:
                dwarves = [hats[k] for k in range(9) if k != i and k != j]
                dwarves.sort()
                for dwarf in dwarves:
                    print(dwarf)
                return

find_dwarves()