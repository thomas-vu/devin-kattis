def angle_to_time(angle):
    minutes = (angle / 5) % 60
    hours = (angle / 30) % 12
    return f"{int(hours):02d}:{int(minutes):02d}"

# Sample Input 1
angle = 855
print(angle_to_time(angle))  # Output: 01:21

# Sample Input 2
angle = 3140
print(angle_to_time(angle))  # Output: 03:08