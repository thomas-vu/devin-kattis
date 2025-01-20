def find_triangle_drama(N, potentials):
    max_potential = -1
    best_trio = (-1, -1, -1)
    
    for i in range(N):
        for j in range(i+1, N):
            if potentials[i][j] != 0:
                for k in range(j+1, N):
                    if potentials[i][k] != 0 and potentials[j][k] != 0:
                        current_potential = potentials[i][j] * potentials[i][k] * potentials[j][k]
                        if current_potential > max_potential:
                            max_potential = current_potential
                            best_trio = (i, j, k)
                        elif current_potential == max_potential:
                            best_trio = min(best_trio, (i, j, k))
    
    return best_trio

# Example usage:
N = int(input())
potentials = [list(map(int, input().split())) for _ in range(N)]
result = find_triangle_drama(N, potentials)
print(*sorted([result[0], result[1], result[2]]))