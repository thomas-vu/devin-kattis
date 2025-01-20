r, f = map(int, input().split())

# Calculate the number of full rotations made by the pan
full_rotations = f // r

# Calculate the angle of the pan after full_rotations rotations
angle = (full_rotations * 360) % 360

# Determine the position of the blueberry side
if angle == 0:
    print("up")
else:
    print("down")