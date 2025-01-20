def min_gold_coins(heads, knights):
    heads.sort()
    knights.sort()
    
    total_cost = 0
    knight_idx = 0
    
    for head in heads:
        while knight_idx < len(knights) and knights[knight_idx] < head:
            knight_idx += 1
        if knight_idx == len(knights):
            return "Loowater is doomed!"
        total_cost += knights[knight_idx]
        knight_idx += 1
    
    return total_cost

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    heads = [int(input()) for _ in range(n)]
    knights = [int(input()) for _ in range(m)]
    
    result = min_gold_coins(heads, knights)
    print(result)