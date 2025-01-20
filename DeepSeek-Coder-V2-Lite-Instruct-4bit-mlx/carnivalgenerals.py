def main():
    N = int(input())
    rankings = [list(map(int, input().split())) for _ in range(N-1)]
    
    # Create a list to store the position of each general in their ranking
    positions = [0] * N
    
    # Fill the position list based on the rankings
    for i in range(N-1):
        ranking = rankings[i]
        for j, pos in enumerate(ranking):
            positions[pos] = i - j
    
    # Sort the generals based on their position in the rankings
    sorted_generals = sorted(range(N), key=lambda x: positions[x])
    
    # Output the sorted order of generals
    print(' '.join(map(str, sorted_generals)))

if __name__ == "__main__":
    main()