def count_patterns(turn_sequence):
    def is_valid(path, next_pivot):
        if next_pivot in path:
            return False
        x1, y1 = divmod(path[-1] - 1, 3)
        x2, y2 = divmod(next_pivot - 1, 3)
        if abs(x1 - x2) + abs(y1 - y2) == 2 and (x1, y1, x2, y2) not in jumps:
            return False
        return True

    def backtrack(path):
        if len(path) == 8:
            return 1
        count = 0
        for next_pivot in range(1, 10):
            if is_valid(path, next_pivot):
                count += backtrack(path + [next_pivot])
        return count

    jumps = {(1, 3): 2, (1, 7): 4, (1, 9): 5, (2, 8): 5, (3, 1): 2, (3, 7): 5, (3, 9): 6,
             (4, 6): 5, (6, 4): 5, (7, 1): 4, (7, 3): 5, (7, 9): 8, (8, 2): 5,
             (9, 1): 5, (9, 3): 6, (9, 7): 8}
    
    result = backtrack([1]) if turn_sequence[0] == '?' else 0
    result += backtrack([2]) if turn_sequence[0] == '?' else 0
    result += backtrack([5]) if turn_sequence[0] == '?' else 0
    
    return result

# Test cases
print(count_patterns("LRRRSRL"))  # Output: 44
print(count_patterns("??AS???"))  # Output: 0