def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        toys_count = {}
        for _ in range(N):
            toy, count = input().split()
            count = int(count)
            if toy in toys_count:
                toys_count[toy] += count
            else:
                toys_count[toy] = count
        
        # Sort by count in descending order, then by toy name in ascending order
        sorted_toys = sorted(toys_count.items(), key=lambda x: (-x[1], x[0]))
        
        # Output the results
        print(len(sorted_toys))
        for toy, count in sorted_toys:
            print(toy, count)

if __name__ == "__main__":
    main()