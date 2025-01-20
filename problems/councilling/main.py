from collections import defaultdict, deque

def solve(test_cases):
    results = []
    for case in test_cases:
        n, residents = parse_input(case)
        graph = defaultdict(list)
        in_degree = {i: 0 for i in range(n)}
        out_degree = defaultdict(int)
        
        for i, resident in enumerate(residents):
            clubs = resident[2]
            for club in clubs:
                graph[club].append(i)
                out_degree[i] += 1
                in_degree[i] += 1
        
        queue = deque()
        for i in range(n):
            if in_degree[i] == out_degree[i]:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if out_degree[neighbor] > 0:
                    out_degree[neighbor] -= 1
                    in_degree[neighbor] -= 1
                    if out_degree[neighbor] == in_degree[neighbor]:
                        queue.append(neighbor)
        
        valid = True
        for i in range(n):
            if out_degree[i] != 0:
                valid = False
                break
        
        if valid:
            for club, members in out_degree.items():
                for member in graph[club]:
                    results.append((member, club))
        else:
            results.append("Impossible.")
    
    return results

def parse_input(case):
    n = case[0]
    residents = []
    for resident_info in case[1:]:
        resident_data = resident_info.split()
        residents.append(resident_data)
    return n, residents

# Main function to read input and output results
def main():
    T = int(input().strip())
    test_cases = []
    for _ in range(T):
        n = int(input().strip())
        case = []
        for _ in range(n):
            case.append(input().strip())
        test_cases.append(case)
    
    results = solve(test_cases)
    for result in results:
        print(result)
        if isinstance(result, str):
            continue
        for member in result:
            print(member[0], member[1])
        if _ != T - 1:
            print()

if __name__ == "__main__":
    main()