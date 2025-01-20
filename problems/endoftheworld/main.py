def moves_remaining(configuration):
    # Count the number of disks and their current positions
    n = len(configuration)
    pegs = {'A': [], 'B': [], 'C': []}
    
    # Populate the pegs with disks based on configuration
    for i, pos in enumerate(configuration):
        pegs[pos].append(n - i)
    
    # Function to count the number of moves required to solve the Towers of Hanoi
    def hanoi_moves(n, source, target, auxiliary):
        if n == 1:
            return 1
        else:
            moves = 0
            # Move n-1 disks from source to auxiliary, so the largest disk is left on source
            moves += hanoi_moves(n - 1, source, auxiliary, target)
            # Move the nth disk directly to the target
            moves += 1
            # Move the n-1 disks on auxiliary to the target
            moves += hanoi_moves(n - 1, auxiliary, target, source)
            return moves
    
    # Calculate the total number of moves required to solve the problem
    total_moves = hanoi_moves(n, 'A', 'B', 'C')
    
    # Count the number of moves already made based on the configuration
    moves_made = 0
    for peg in pegs.values():
        if len(peg) > 1:
            # If there are multiple disks on a peg, they must have been moved at least once
            moves_made += len(peg) - 1
    
    # The number of moves remaining is the total required minus the moves already made
    return total_moves - moves_made

# Read input until 'X' is encountered
while True:
    configuration = input().strip()
    if configuration == 'X':
        break
    print(moves_remaining(configuration))