def check_proof(n, lines):
    assumptions = []
    for i in range(1, n + 1):
        line = lines[i - 1]
        parts = line.split()
        assumptions_line = parts[:-2]
        conclusion = parts[-1]
        
        if all(assumption in assumptions for assumption in assumptions_line):
            assumptions.append(conclusion)
        else:
            return i
    return "correct"

# Read input from stdin
n = int(input().strip())
lines = [input().strip() for _ in range(n)]

# Check the proof and output the result
result = check_proof(n, lines)
print(result)