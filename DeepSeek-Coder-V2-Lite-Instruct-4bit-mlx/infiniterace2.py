N = int(input())
Q = int(input())
events = [int(input()) for _ in range(Q)]

laps_completed = 0
positions = [0] * (N - 1)

for event in events:
    if event > 0:
        # Anika overtakes participant
        for i in range(N - 1):
            if positions[i] < event:
                positions[i] = -1  # Mark as overtaken by Anika
    else:
        # Anika is overtaken by participant
        x_i = -event
        for i in range(N - 1):
            if positions[i] < 0:
                continue
            if positions[i] > x_i:
                positions[i] = -1  # Mark as overtaken by participant i
            elif positions[i] < x_i:
                positions[i] = 1  # Mark as overtaking participant i

    for pos in positions:
        if pos == 1:
            # Anika has overtaken someone
            laps_completed += 1
            for i in range(N - 1):
                if positions[i] == 0:
                    positions[i] = -1
        elif pos == -1:
            # Anika has been overtaken
            for i in range(N - 1):
                if positions[i] == 0:
                    positions[i] = 1

    # Update positions after each event
    for i in range(N - 1):
        if positions[i] == -1:
            positions[i] = 0
        elif positions[i] == 1:
            positions[i] = -1

print(laps_completed + 1)