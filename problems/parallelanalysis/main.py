def min_parallel_time(instructions):
    n = len(instructions)
    max_dependencies = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if any(ref == instructions[j][0] for ref in instructions[i][1:]):
                max_dependencies[j] = max(max_dependencies[j], max_dependencies[i] + 1)
    
    return max(max_dependencies) + n

def main():
    t = int(input())
    for case_number in range(1, t + 1):
        n = int(input())
        instructions = []
        for _ in range(n):
            line = list(map(int, input().split()))
            m = line[0]
            mem_refs = line[1:]
            instructions.append(mem_refs)
        
        min_time = min_parallel_time(instructions)
        print(f"Case #{case_number}: {min_time}")

if __name__ == "__main__":
    main()