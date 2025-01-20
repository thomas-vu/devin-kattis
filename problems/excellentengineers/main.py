def find_shortlist(n, engineers):
    min_ranks = [float('inf'), float('inf'), float('inf')]
    for engineer in engineers:
        min_ranks = [min(min_ranks[i], engineer[i]) for i in range(3)]
    
    shortlist_count = 0
    for engineer in engineers:
        if all(engineer[i] == min_ranks[i] for i in range(3)):
            shortlist_count += 1
    
    return shortlist_count

def main():
    num_test_cases = int(input().strip())
    results = []
    
    for _ in range(num_test_cases):
        n = int(input().strip())
        engineers = []
        for _ in range(n):
            r1, r2, r3 = map(int, input().strip().split())
            engineers.append((r1, r2, r3))
        
        results.append(find_shortlist(n, engineers))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()