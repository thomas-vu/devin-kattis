def generate_crossword(A, B):
    N = len(A)
    M = len(B)
    
    # Find the index of the first common letter in A and B
    for i, char in enumerate(A):
        if char in B:
            first_common_index = i
            break
    
    # Create the crossword grid
    crossword = [['.' for _ in range(N)] for _ in range(M)]
    
    # Place the words in the crossword grid
    for i, char in enumerate(B):
        crossword[i][first_common_index] = char
    
    for i, char in enumerate(A):
        crossword[first_common_index][i] = char
    
    # Output the crossword grid
    for row in crossword:
        print(''.join(row))

# Read input
A, B = input().split()
generate_crossword(A, B)