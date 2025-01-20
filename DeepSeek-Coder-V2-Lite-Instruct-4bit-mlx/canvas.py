def min_ink_cost(sizes):
    total_sum = sum(sizes)
    unique_colors = set()
    ink_cost = 0
    
    for size in sizes:
        if size not in unique_colors:
            ink_cost += size
            unique_colors.add(size)
    
    return ink_cost

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        N = int(input())
        sizes = list(map(int, input().split()))
        results.append(min_ink_cost(sizes))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()