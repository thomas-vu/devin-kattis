def can_survive(N, M, P, damages):
    health = N
    for damage in damages:
        health -= damage
        while health < 0 and P > 0:
            health += 20
            P -= 1
        if health <= 0:
            return "next time"
    return "champion"

# Read input
N, M, P = map(int, input().split())
damages = list(map(int, input().split()))

# Determine if the Pokemon can survive
result = can_survive(N, M, P, damages)
print(result)