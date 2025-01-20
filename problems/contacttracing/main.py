def spread_of_virus(N, D, C, infected, entries):
    infection_status = [False] * (N + 1)
    for infected_person in infected:
        infection_status[infected_person] = True
    
    for day in range(D):
        new_infections = [False] * (N + 1)
        for i in range(1, N + 1):
            if infection_status[i]:
                for j in range(1, N + 1):
                    if entries[i][0] <= entries[j][0] <= entries[i][1] or entries[i][0] <= entries[j][1] <= entries[i][1]:
                        new_infections[j] = True
        infection_status = [x or y for x, y in zip(infection_status, new_infections)]
    
    infected_after_D_days = [i for i in range(1, N + 1) if infection_status[i]]
    return infected_after_D_days

# Read input
N, D = map(int, input().split())
C = list(map(int, input().split()))
entries = [list(map(int, input().split())) for _ in range(N)]

# Get the result
infected_after_D_days = spread_of_virus(N, D, C[0], C[1:], entries)

# Print the result
print(' '.join(map(str, infected_after_D_days)))