def can_simulate(dice):
    # Convert the probabilities to a matrix where each row represents a die and each column represents an outcome
    dice_matrix = [row[:3] for row in dice]
    
    # Check if the sum of probabilities for each die is 10000
    for row in dice_matrix:
        if sum(row) != 10000:
            return "NO"
    
    # Check if we can simulate the desired die using linear combinations of the given dice
    desired_prob = dice[-1][:3]
    
    # Check if we can find coefficients a, b, c such that:
    # a*dice1 + b*dice2 + c*dice3 = desired_prob
    # This is a system of linear equations, we can solve it using Gaussian elimination or matrix inversion
    
    # Construct the augmented matrix [dice1, dice2, dice3 | desired_prob]
    aug_matrix = [list(dice_matrix[i]) + [desired_prob[i]] for i in range(3)]
    
    # Perform Gaussian elimination to check if the system is consistent
    for i in range(3):
        # Find the pivot element
        pivot = aug_matrix[i][i]
        if pivot == 0:
            return "NO"
        
        # Normalize the row by the pivot element
        for j in range(6):
            aug_matrix[i][j] /= pivot
        
        # Eliminate the current column in all other rows
        for k in range(3):
            if k != i:
                factor = aug_matrix[k][i]
                for j in range(6):
                    aug_matrix[k][j] -= factor * aug_matrix[i][j]
    
    # Check if the augmented matrix is consistent by looking at the last column
    for i in range(3):
        if aug_matrix[i][-1] != 0:
            return "NO"
    
    return "YES"

# Read input and process each test case
import sys
input = sys.stdin.read
data = input().split()
dice_list = []
i = 0
while i < len(data):
    dice = [list(map(int, data[i:i+3])) for i in range(0, 12, 3)]
    dice_list.append(dice)
    i += 12

# Output the results for each test case
for dice in dice_list:
    if len(dice) == 4:
        print(can_simulate(dice))