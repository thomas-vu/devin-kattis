def solve_cryptarithm(puzzle):
    words = puzzle.split('+')
    left_side = words[0].strip()
    right_side = words[1].strip().split('=')[0]
    result = words[1].strip().split('=')[1]
    
    # Extract all unique letters from the puzzle
    letters = set(left_side + right_side + result)
    
    # Helper function to convert letters to digits
    def assign_digits(assignment, letters):
        mapping = {}
        for letter in letters:
            if letter not in assignment:
                # Assign the smallest unused digit
                for digit in range(10):
                    if str(digit) not in assignment.values():
                        mapping[letter] = digit
                        break
            else:
                # Use the existing assignment for this letter
                mapping[letter] = assignment[letter]
        return mapping
    
    # Helper function to check if the current assignment is valid
    def is_valid(mapping, left_side, right_side, result):
        num1 = ''.join(str(mapping[char]) for char in left_side)
        num2 = ''.join(str(mapping[char]) for char in right_side)
        num3 = ''.join(str(mapping[char]) for char in result)
        
        return int(num1) + int(num2) == int(num3)
    
    # Generate all possible assignments of digits to letters
    from itertools import permutations
    
    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))
        if is_valid(assignment, left_side, right_side, result):
            # Convert letters to digits in the puzzle
            solution = assign_digits(assignment, letters)
            # Convert left side and right side to numbers and check the equality
            num1 = int(''.join(str(solution[char]) for char in left_side))
            num2 = int(''.join(str(solution[char]) for char in right_side))
            num3 = int(''.join(str(solution[char]) for char in result))
            
            if num1 + num2 == num3:
                # Return the solution with letters replaced by digits
                return {chr(ord('A') + i): str(solution[chr(ord('A') + i)]) for i in range(len(letters))}
    
    return "impossible"

# Test the function with the given examples
puzzle1 = "SEND+MORE=MONEY"
puzzle2 = "A+A=A"
puzzle3 = "C+B=A"

print(solve_cryptarithm(puzzle1))  # Expected output: {'S': '9', 'E': '5', 'N': '6', 'D': '7', 'M': '1', 'O': '0', 'R': '8', 'Y': '2'}
print(solve_cryptarithm(puzzle2))  # Expected output: "impossible"
print(solve_cryptarithm(puzzle3))  # Expected output: {'C': '2', 'B': '1', 'A': '3'}