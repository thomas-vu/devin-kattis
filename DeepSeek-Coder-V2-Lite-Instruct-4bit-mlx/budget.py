def solve_budget_proposal():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(test_cases):
        m = int(data[index])
        n = int(data[index + 1])
        row_sums = list(map(int, data[index + 2].split()))
        col_sums = list(map(int, data[index + 3].split()))
        k = int(data[index + 4])
        constraints = []
        for i in range(5, 5 + k):
            r, c = map(int, data[i].split())
            op, v = data[i + 1].split()
            constraints.append((r, c, op, int(v)))
            i += 2
        
        matrix = [[0] * n for _ in range(m)]
        possible = backtrack(matrix, row_sums, col_sums, constraints)
        if possible:
            results.append("\n".join(" ".join(map(str, row)) for row in matrix))
        else:
            results.append("IMPOSSIBLE")
        index += 5 + k
    
    print("\n\n".join(results))

def backtrack(matrix, row_sums, col_sums, constraints):
    if all(sum(row) == row_sum for row in matrix) and all(sum(col) == col_sum for col in zip(*matrix)):
        return True
    
    r, c = len(matrix), len(matrix[0]) if matrix else (len(row_sums), len(col_sums))
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                for value in range(1, 1001):
                    matrix[i][j] = value
                    if check_constraints(matrix, constraints, i, j, value) and backtrack(matrix, row_sums, col_sums, constraints):
                        return True
                    matrix[i][j] = 0
                return False
    return False

def check_constraints(matrix, constraints, i, j, value):
    for r, c, op, v in constraints:
        if (r == -1 or r == i) and (c == -1 or c == j):
            if op == '<' and value >= v:
                return False
            elif op == '=' and value != v:
                return False
            elif op == '>' and value <= v:
                return False
    return True

solve_budget_proposal()