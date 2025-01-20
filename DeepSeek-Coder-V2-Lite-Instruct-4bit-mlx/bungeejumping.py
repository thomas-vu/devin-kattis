def calculate_scenario(k, l, s, w):
    # Calculate the speed at which James Bond would hit the ground if the rope is too short or just right
    g = 9.81
    weight_force = w * g
    rope_stretched = k * (l - s)
    
    if rope_stretched < weight_force:
        # The rope is too short or just right, James Bond will be stuck in the air
        return "Stuck in the air."
    else:
        # The rope is too long, calculate the speed at impact
        total_force = weight_force + rope_stretched
        acceleration = total_force / w
        impact_speed = (2 * g * s) ** 0.5
        
        if impact_speed > 10:
            # James Bond will be killed by the impact
            return "Killed by the impact."
        else:
            # James Bond survives with a comfortable speed
            return "James Bond survives."

while True:
    k, l, s, w = map(float, input().split())
    if k == 0 and l == 0 and s == 0 and w == 0:
        break
    result = calculate_scenario(k, l, s, w)
    print(result)