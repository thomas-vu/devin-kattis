def can_construct_angle(initial_angles, target_angle):
    from itertools import product
    
    # Mirko can construct the angle by adding or subtracting known angles
    def check_constructible(target, known_angles):
        for angles in product([1, -1], repeat=len(known_angles)):
            angle_sum = sum(angle * coeff for angle, coeff in zip(known_angles, angles))
            if abs(angle_sum - target) < 1e-6:  # Allow for floating point precision
                return True
        return False
    
    known_angles = set(initial_angles)
    for angle in target_angle:
        if check_constructible(angle, known_angles):
            print("YES")
        else:
            print("NO")
            
# Read input
N, K = map(int, input().split())
initial_angles = list(map(int, input().split()))
target_angle = list(map(int, input().split()))

# Process each target angle
can_construct_angle(initial_angles, target_angle)