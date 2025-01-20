def max_coins(P, N1, N5, N10, N25):
    total_value = N1 + 5 * N5 + 10 * N10 + 25 * N25
    if total_value < P:
        return "Impossible"
    
    coins = [N25, N10, N5, N1]
    values = [25, 10, 5, 1]
    
    used_coins = 0
    for i in range(4):
        if P >= values[i]:
            min_coins = min(P // values[i], coins[i])
            P -= min_coins * values[i]
            used_coins += min_coins
    
    return used_coins if P == 0 else "Impossible"

P = int(input())
N1, N5, N10, N25 = map(int, input().split())
print(max_coins(P, N1, N5, N10, N25))