def check_collision(N, brooms):
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1, r1 = brooms[i]
            x2, y2, r2 = brooms[j]
            
            # Calculate the positions of the two ends of each broom
            end1_x = x1 + 0.5 * (1 - r1)
            end1_y = y1 + 0.5 * (1 - r1)
            end2_x = x1 + 0.5 * (1 + r1)
            end2_y = y1 + 0.5 * (1 + r1)
            
            end3_x = x2 + 0.5 * (1 - r2)
            end3_y = y2 + 0.5 * (1 - r2)
            end4_x = x2 + 0.5 * (1 + r2)
            end4_y = y2 + 0.5 * (1 + r2)
            
            # Check for overlap in the x-direction
            if not (end1_x > end4_x or end2_x < end3_x):
                # Check for overlap in the y-direction
                if not (end1_y > end4_y or end2_y < end3_y):
                    return "crash"
    return "ok"

# Read input
N = int(input().strip())
brooms = [tuple(map(float, input().strip().split())) for _ in range(N)]

# Check for collisions and output the result
result = check_collision(N, brooms)
print(result)