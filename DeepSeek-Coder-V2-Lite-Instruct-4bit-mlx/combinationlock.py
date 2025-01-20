def calculate_degrees(initial, combination):
    # Define the total degrees in a circle
    total_degrees = 360
    
    # Calculate the number of degrees for each segment of the combination
    first_segment = (combination[0] - initial) % 40 * 90
    second_segment = ((initial - combination[1]) % 40 + 40) % 40 * 90
    third_segment = (combination[2] - combination[1]) % 40 * 90
    
    # Sum up the degrees for all segments
    total_degrees_turned = first_segment + second_segment + third_segment
    
    return total_degrees_turned

# Main loop to process input and output results
while True:
    # Read the input for each test case
    inputs = list(map(int, input().split()))
    
    # Break the loop if all inputs are zeros
    if inputs == [0, 0, 0, 0]:
        break
    
    # Extract the initial position and combination from the input
    initial_position = inputs[0]
    combination = inputs[1:]
    
    # Calculate the total degrees turned to open the lock
    result = calculate_degrees(initial_position, combination)
    
    # Output the result for each test case
    print(result)