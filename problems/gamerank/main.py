def update_rank(current_rank, stars):
    if current_rank == 25:
        return 25
    rank_stars = {
        25: [1, 2],
        24: [1, 2],
        23: [1, 2],
        22: [1, 2],
        21: [2],
        20: [2],
        19: [3],
        18: [3],
        17: [3],
        16: [3],
        15: [4],
        14: [4],
        13: [4],
        12: [4],
        11: [5],
        10: [5],
        9: [5],
        8: [5],
        7: [5],
        6: [5],
        5: [5],
        4: [5],
        3: [5],
        2: [5],
        1: [5]
    }
    
    if stars == len(rank_stars[current_rank]):
        return max(1, current_rank - 1)
    else:
        return current_rank

def process_sequence(seq):
    rank = 25
    stars = 0
    
    for game in seq:
        if game == 'W':
            stars += 1
            if rank <= 20 and stars > len(rank_stars[rank]):
                stars = 1
                rank -= 1
            elif rank <= 20 and stars == len(rank_stars[rank]):
                stars = 1 if rank != 20 else 0
                rank -= 1
        elif game == 'L':
            stars = max(0, stars - 1)
            if rank <= 20 and stars == -1:
                rank += 1
                stars = len(rank_stars[rank]) - 1
    
    if rank == 25 and stars >= len(rank_stars[rank]):
        return "Legend"
    else:
        return rank

# Read input from stdin
seq = input().strip()
result = process_sequence(seq)
print(result)