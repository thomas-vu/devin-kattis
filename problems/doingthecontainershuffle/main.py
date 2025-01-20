def expected_moves(n, order):
    # Initialize the stacks and the moves count
    stack1 = []
    stack2 = []
    total_moves = 0
    
    # Process each container in the order they are to be loaded onto trucks
    for container in order:
        # Check if the container is on top of stack1
        if stack1 and stack1[-1] == container:
            # Move the container from stack1 to truck
            stack1.pop()
        elif stack2 and stack2[-1] == container:
            # Move the container from stack2 to truck
            stack2.pop()
        else:
            # Move containers from the stacks to get the container on top of its stack
            while stack1 and stack1[-1] != container:
                moves_to_move = 0
                while stack1:
                    temp = stack1.pop()
                    moves_to_move += 1
                    stack2.append(temp)
                total_moves += moves_to_move
            while stack2 and stack2[-1] != container:
                moves_to_move = 0
                while stack2:
                    temp = stack2.pop()
                    moves_to_move += 1
                    stack1.append(temp)
                total_moves += moves_to_move
            # Move the container from its original stack to truck
            if stack1:
                stack1.pop()
            elif stack2:
                stack2.pop()
        # Move the container from truck to top of its stack if necessary (not needed in this context)
        # total_moves += 1  # This is commented out because the container is already on top of its stack
    
    return total_moves

# Main function to read input and compute the expected number of moves
def main():
    n = int(input())
    order = list(map(int, input().split()))
    
    # Calculate the expected number of moves
    expected_moves_count = expected_moves(n, order)
    
    # Print the result with an absolute error of at most 10^-3
    print("{:.3f}".format(expected_moves_count))

# Call the main function
if __name__ == "__main__":
    main()