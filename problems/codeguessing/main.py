def determine_digits(p, q):
    # Create a list to store all possible combinations of Bob's cards
    possible_combinations = []
    
    # Generate all permutations of the digits excluding Alice's cards
    from itertools import permutations
    for combo in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]):
        if list(combo[:2]) == [p, q]:
            continue
        possible_combinations.append(list(combo[:2]))
    
    # Parse the positions of Alice's and Bob's cards
    positions = list(input().strip())
    alice_positions = [i for i, pos in enumerate(positions) if pos == 'A']
    bob_positions = [i for i, pos in enumerate(positions) if pos == 'B']
    
    # Filter possible combinations based on the positions of Alice's cards
    filtered_combinations = []
    for combo in possible_combinations:
        if (p < combo[0] and q < combo[1]) or (p > combo[0] and q > combo[1]):
            filtered_combinations.append(combo)
    
    # Check if there is a unique combination that fits the conditions
    if len(filtered_combinations) == 1:
        # Output the unique combination sorted in ascending order
        for digit in filtered_combinations[0]:
            print(digit, end='')
    else:
        # Output -1 if there is no unique solution
        print(-1)

# Read the input
p, q = map(int, input().split())
determine_digits(p, q)