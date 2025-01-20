while True:
    w, l = map(int, input().split())
    if w == 0 and l == 0:
        break
    
    x, y = 0, 0
    for _ in range(n):
        direction, steps = input().split()
        steps = int(steps)
        
        if direction == 'u':
            y += steps
        elif direction == 'd':
            y -= steps
        elif direction == 'l':
            x -= steps
        elif direction == 'r':
            x += steps
    
    print(f"Robot thinks {x} {y}")
    
    # Assuming the robot's position is calculated correctly based on the path
    print(f"Actually at {w-1 if x < 0 else 0} {l-1 if y < 0 else 0}")