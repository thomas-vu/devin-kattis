def count_winning_moves(numbers):
    n = len(numbers)
    odd_count = [num for num in numbers if num % 2 == 1]
    even_count = [num for num in numbers if num % 2 == 0]
    
    # If the number of odd numbers is even, Zvonko wins regardless of who starts.
    if len(odd_count) % 2 == 0:
        return 0
    
    # If the number of odd numbers is odd, Ivana can win by making a move.
    return 1

# Read input
N = int(input())
numbers = list(map(int, input().split()))

# Get the number of winning first moves for Ivana
winning_moves = count_winning_moves(numbers)

# Output the result
print(winning_moves)