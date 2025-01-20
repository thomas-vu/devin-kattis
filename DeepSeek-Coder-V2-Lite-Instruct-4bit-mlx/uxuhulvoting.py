def find_outcome(preferences):
    # Convert preferences to binary representation for easier comparison
    prefs = [bin(pref)[2:].zfill(3) for pref in preferences]
    
    # Initialize the outcome of each issue to 'N' (no)
    outcomes = ['N', 'N', 'N']
    
    # Iterate over each preference to determine the outcome of each issue
    for pref in prefs:
        # Determine which issues should be flipped based on preference order
        for i, bit in enumerate(pref):
            if bit == '1':  # If the preference is higher, flip the issue to 'Y' (yes)
                outcomes[i] = 'Y'
            else:  # If the preference is lower, do nothing as it defaults to 'N'
                break
    
    # Join the outcomes into a single string and return
    return ''.join(outcomes)

# Read number of voting rounds
n = int(input())

# Process each voting round
for _ in range(n):
    # Read number of voting priests
    m = int(input())
    
    # Read preferences for each voter
    preferences = [int(input()) for _ in range(m)]
    
    # Find and print the outcome of the votes
    outcome = find_outcome(preferences)
    print(outcome)