def calculate_discontentment(n, m, dislike_pairs, q, instructions):
    # Initialize the line with all cat recruits
    line = list(range(1, n + 1))
    
    # Process each instruction and calculate the discontentment sum after each step
    results = []
    for instruction in instructions:
        if instruction[0] == 1:
            # Move cat recruit i into the line
            position = instruction[1] - 1
            line.insert(position, position)
        else:
            # Move cat recruit i out of the line
            position = instruction[1] - 1
            line.pop(position)
        
        # Calculate the sum of discontentment after each instruction
        sum_discontentment = 0
        for i in range(len(line)):
            left_neighbor = line[i - 1] if i > 0 else None
            right_neighbor = line[i + 1] if i < len(line) - 1 else None
            if left_neighbor is not None and right_neighbor is not None:
                if (left_neighbor, i + 1) in dislike_pairs and (i + 1, right_neighbor) in dislike_pairs:
                    sum_discontentment += 3233
                elif left_neighbor == i + 1 or right_neighbor == i + 1:
                    sum_discontentment += 323
                else:
                    sum_discontentment += 32 if left_neighbor == i + 1 else (3 if right_neighbor == i + 1 else 3)
        
        results.append(sum_discontentment)
    
    return results

# Read input
n, m = map(int, input().split())
dislike_pairs = set()
for _ in range(m):
    x, y = map(int, input().split())
    dislike_pairs.add((x - 1, y - 1))
q = int(input())
instructions = [list(map(int, input().split())) for _ in range(q)]

# Calculate and output the results
results = calculate_discontentment(n, m, dislike_pairs, q, instructions)
for result in results:
    print(result)