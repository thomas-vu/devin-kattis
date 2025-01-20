def read_ints():
    return list(map(int, input().split()))

# Read the number of folds, cuts, and length of the paper
N, M, L = read_ints()
# Read the fold positions
folds = read_ints()
# Read the cut positions
cuts = read_ints()

# Function to simulate the folding process and determine the lengths of each pile after cuts
def simulate_folding(folds, cuts):
    # Initialize the paper as a list of zeros with length L+1 to account for positions from 0 to L
    paper = [0] * (L + 1)
    
    # Simulate the folding process from right to left
    for fold in reversed(folds):
        # Place a marker at the fold position
        paper[fold] = 1
    
    # Perform the cuts from left to right
    for cut in cuts:
        count = 0
        # Count the number of layers to the left of the cut
        for i in range(cut, -1, -1):
            if paper[i] == 1:
                count += 1
            else:
                break
        # The pile at the cut position will have 'count' layers of paper
        print(count, end=' ')
    # The last pile after the final cut
    count = 0
    for i in range(L, -1, -1):
        if paper[i] == 1:
            count += 1
        else:
            break
    print(count)

# Call the simulation function with the given inputs
simulate_folding(folds, cuts)