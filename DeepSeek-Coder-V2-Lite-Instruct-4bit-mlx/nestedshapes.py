def calculate_area(shape, side):
    if shape == 'C':
        return 3.141592653589793 * side**2
    elif shape == 'S':
        return side**2
    else:  # D for diamond
        return 2 * side**2

def calculate_perimeter(shape, side):
    if shape == 'C':
        return 2 * 3.141592653589793 * side
    elif shape == 'S':
        return 4 * side
    else:  # D for diamond
        return 8 * side / (2**0.5)

def main():
    n, shapes = input().split()
    n = int(n)
    shape_list = list(shapes)
    t1, m = input().split()
    tn, _ = input().split()
    
    # Determine the initial shape and dimension based on t1
    if t1 == 'A':
        area_R1 = m
        side_R1 = (area_R1 / (3.141592653589793 if shape_list[0] == 'C' else 2))**0.5
    else:
        perimeter_R1 = m
        side_R1 = perimeter_R1 / (4 if shape_list[0] == 'S' else 8 * (2**0.5))
    
    # Calculate areas and perimeters for each subsequent region
    current_side = side_R1
    for i in range(1, n):
        if shape_list[i] == 'C':
            current_area = 3.141592653589793 * current_side**2
            next_side = (current_area / (3.141592653589793 if shape_list[i-1] == 'C' else 2))**0.5
        elif shape_list[i] == 'S':
            next_side = current_side * (2**0.5) / 2
        else:  # D for diamond
            next_side = current_side / (2**0.5) * 2
        
        # Update the current side for the next iteration
        current_side = next_side
    
    # Determine the final area or perimeter based on tn
    if tn == 'A':
        result = calculate_area(shape_list[-1], current_side)
    else:
        result = calculate_perimeter(shape_list[-1], current_side)
    
    print("{:.16f}".format(result))

main()