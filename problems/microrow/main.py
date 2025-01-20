def min_rows(N, microbes):
    # Sort microbes by their final position (P_i + S_i * time)
    # where time is some future point in time. We can use the initial positions for sorting since S_i > 0.
    microbes = sorted([(P_i, S_i, i) for i, (P_i, S_i) in enumerate(microbes)], key=lambda x: x[0] + x[1])
    
    # Assign rows based on the sorted order without overlapping
    assigned_rows = [0] * N
    current_row = 1
    
    for i in range(N):
        if assigned_rows[microbes[i][2]] == 0:
            assigned_rows[microbes[i][2]] = current_row
            for j in range(i + 1, N):
                if microbes[j][0] + microbes[j][1] * (i - j) <= microbes[i][0]:
                    assigned_rows[microbes[j][2]] = current_row
                else:
                    break
            current_row += 1
    
    return assigned_rows

# Read input
N = int(input())
microbes = [tuple(map(int, input().split())) for _ in range(N)]

# Get the rows assignment
rows = min_rows(N, microbes)

# Output the result
print(" ".join(map(str, rows)))