def compare_shots(a, b):
    total_alcohol_a = 0
    total_alcohol_b = 0
    
    for _ in range(a):
        v, c = map(int, input().split())
        total_alcohol_a += v * (c / 100)
    
    for _ in range(b):
        v, c = map(int, input().split())
        total_alcohol_b += v * (c / 100)
    
    if abs(total_alcohol_a - total_alcohol_b) < 1e-9:
        print("same")
    else:
        print("different")

# Read the number of ingredients for each shot
a, b = map(int, input().split())
compare_shots(a, b)