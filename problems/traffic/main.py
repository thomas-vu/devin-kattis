X1, X2 = map(int, input().split())
N1 = int(input())
T1 = list(map(int, input().split()))
N2 = int(input())
T2 = list(map(int, input().split()))

# Initialize the positions of the cars
pos1 = X1
pos2 = X2
time_collision = -1

# Process the speed changes for both cars
for i in range(0, max(N1, N2), 2):
    speed1 = 1 if i < N1 else -1
    speed2 = 1 if i + 1 < N2 else -1
    
    # Calculate the positions of the cars at each speed change time
    for t in T1[i//2 if i < N1 else (N1-1)//2*2 - i]:
        pos1 += speed1
    for t in T2[(i+1)//2 if i+1 < N2 else (N2-1)//2*2 - (i+1)]:
        pos2 += speed2
    
    # Check for collision
    if pos1 + 4.4 <= pos2 and speed1 == -1 and speed2 == -1:
        time_collision = max(t, (X2 - X1) / (speed1 + speed2))
        break
    elif pos2 + 4.4 <= pos1 and speed1 == -1 and speed2 == -1:
        time_collision = max(t, (X1 - X2) / (speed1 + speed2))
        break

# Output the result
if time_collision != -1:
    print(f"bumper tap at time {int(time_collision + 0.5)}")
else:
    print("safe and sound")