def count_switches(search_engines, queries):
    switches = 0
    current_engine = None
    
    for query in queries:
        if query not in search_engines:
            continue
        
        if current_engine is None or query != current_engine:
            current_engine = query
            switches += 1
    
    return switches - 1 if current_engine is not None else 0

def main():
    T = int(input())
    for case in range(1, T + 1):
        S = int(input())
        search_engines = [input().strip() for _ in range(S)]
        Q = int(input())
        queries = [input().strip() for _ in range(Q)]
        
        switches = count_switches(search_engines, queries)
        print(f"Case #{case}: {switches}")

if __name__ == "__main__":
    main()