import sys

def generate_unique_expressions(n, pairs):
    operators = ['+', '-', '*']
    results = set()
    
    for a, b in pairs:
        valid_expressions = []
        for op in operators:
            try:
                result = eval(f"{a}{op}{b}")
                if result not in results:
                    valid_expressions.append(f"{a} {op} {b} = {result}")
                    results.add(result)
            except:
                pass
        
        if len(valid_expressions) == 0:
            return "impossible"
        elif len(valid_expressions) > 1:
            raise ValueError("Multiple valid expressions found for a pair")
        else:
            print(valid_expressions[0])

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    pairs = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    generate_unique_expressions(n, pairs)