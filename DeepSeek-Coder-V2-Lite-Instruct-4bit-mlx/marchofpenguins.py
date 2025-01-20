def can_meet(floes, D):
    meeting_points = set()
    
    for i in range(len(floes)):
        x1, y1, n_i, m_i = floes[i]
        if n_i == 0:  # No penguins on this floe, it's always a valid meeting point
            meeting_points.add(i)
        else:
            for j in range(len(floes)):
                x2, y2, n_j, m_j = floes[j]
                if j != i and n_j > 0:  # Valid target floe with penguins
                    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                    if distance <= D * m_i:  # Penguins can jump to the target floe
                        meeting_points.add(i)
                        break  # No need to check further targets for this floe
    
    if meeting_points:
        return sorted(list(meeting_points))
    else:
        return [-1]

# Read input
N, D = map(float, input().split())
floes = [list(map(int, input().split())) for _ in range(int(N))]

# Get the result and print it
result = can_meet(floes, D)
print(*result)