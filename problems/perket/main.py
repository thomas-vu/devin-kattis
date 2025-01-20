def perket():
    N = int(input())
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    
    min_diff = float('inf')
    
    for mask in range(1, 1 << N):
        sourness = 1
        bitterness = 0
        for i in range(N):
            if mask & (1 << i):
                sourness *= ingredients[i][0]
                bitterness += ingredients[i][1]
        min_diff = min(min_diff, abs(sourness - bitterness))
    
    return min_diff

print(perket())