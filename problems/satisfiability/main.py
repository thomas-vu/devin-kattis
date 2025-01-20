def is_satisfiable(n, clauses):
    from itertools import product
    
    # Generate all possible assignments for n variables
    for assignment in product([0, 1], repeat=n):
        satisfiable = True
        for clause in clauses:
            literals = [clause[i] if i % 2 == 0 else -clause[i] for i in range(len(clause))]
            eval_result = any([assignment[abs(lit) - 1] == (1 if lit > 0 else 0) for lit in literals])
            if not eval_result:
                satisfiable = False
                break
        if satisfiable:
            return True
    return False

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        clauses = []
        for _ in range(m):
            clause = data[index]
            index += 1
            clauses.append([int(x) if x[0] == 'X' else -int(x[1:]) for x in clause.split(' v ')])
        if is_satisfiable(n, clauses):
            results.append('satisfiable')
        else:
            results.append('unsatisfiable')
    
    for result in results:
        print(result)

main()