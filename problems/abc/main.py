def rearrange_numbers():
    # Read the input values for A, B, and C
    a, b, c = map(int, input().split())
    
    # Read the order string
    order = input()
    
    # Create a list to hold the numbers in the desired order
    arranged = []
    
    # Rearrange the numbers based on the given order string
    for char in order:
        if char == 'A':
            arranged.append(a)
        elif char == 'B':
            arranged.append(b)
        else:  # char == 'C'
            arranged.append(c)
    
    # Output the rearranged numbers
    print(*arranged)

# Call the function to rearrange and output the numbers
rearrange_numbers()