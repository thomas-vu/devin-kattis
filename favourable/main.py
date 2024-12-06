def count_favorable_paths(graph, start, memo=None):
    if memo is None:
        memo = {}
    
    if start in memo:
        return memo[start]
    
    if start not in graph:
        return 0
    
    if graph[start] == "favourably":
        return 1
    elif graph[start] == "catastrophically":
        return 0
    
    total = 0
    for next_page in graph[start]:
        total += count_favorable_paths(graph, next_page, memo)
    
    memo[start] = total
    return total

def solve_test_case():
    n = int(input())
    graph = {}
    
    for _ in range(n):
        line = input().split()
        page = int(line[0])
        
        if len(line) == 2:  # Ending section
            graph[page] = line[1]  # "favourably" or "catastrophically"
        else:  # Choice section
            graph[page] = [int(line[i]) for i in range(1, 4)]
    
    return count_favorable_paths(graph, 1)

# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    result = solve_test_case()
    print(result)
