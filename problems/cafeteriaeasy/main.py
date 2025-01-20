def fill_plates(top, bottom):
    # Calculate the proportions based on known values
    def calculate_proportions(a, b, c, d):
        ratio = a / b if b != 0 else float('inf')
        return int(c * ratio), int(d * ratio)
    
    # Fill the plates with calculated values
    def fill_plate(index, top_known, bottom_known):
        if index == 0:
            burger1, slop1 = calculate_proportions(top[2], top[3], top[0], top[1])
            burger2, slop2 = calculate_proportions(top[4], top[5], top[2], top[3])
            return burger1, slop1, burger2, slop2
        elif index == 2:
            sushi1, drumstick1 = calculate_proportions(bottom[0], bottom[1], bottom[2], bottom[3])
            sushi2, drumstick2 = calculate_proportions(bottom[4], bottom[5], bottom[6], bottom[7])
            return sushi1, drumstick1, sushi2, drumstick2
        else:
            raise ValueError("Invalid index")
    
    # Process the top and bottom plates separately
    top_filled = [0, 0, int(top[0]), int(top[1]), int(top[2]), int(top[3]), 0, 0, int(top[8]), int(top[9])]
    bottom_filled = [int(bottom[0]), int(bottom[1]), 0, 0, int(bottom[4]), int(bottom[5]), int(bottom[6]), int(bottom[7]), int(bottom[8]), int(bottom[9])]
    
    for i in range(6):
        if top_filled[i * 2] == 0:
            burger, slop = fill_plate(i * 2, top[i * 2], top[i * 2 + 1])
            top_filled[i * 2] = burger
            top_filled[i * 2 + 1] = slop
        if bottom_filled[i * 2] == 0:
            sushi, drumstick = fill_plate(i * 2 + 1, bottom[i * 2], bottom[i * 2 + 1])
            bottom_filled[i * 2] = sushi
            bottom_filled[i * 2 + 1] = drumstick
    
    # Output the filled plates
    top_output = [str(top_filled[i]) if top_filled[i] != 0 else '_' for i in range(10)]
    bottom_output = [str(bottom_filled[i]) if bottom_filled[i] != 0 else '_' for i in range(10)]
    
    print(' '.join(top_output))
    print(' '.join(bottom_output))

# Read input
top = list(map(int, input().split()))
bottom = list(map(int, input().split()))

# Fill and print the plates
fill_plates(top, bottom)