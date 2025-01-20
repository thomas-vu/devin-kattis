import heapq

def main():
    n, k, l = map(int, input().split())
    happiness_ratings = list(map(int, input().split()))
    
    # Sort the happiness ratings in descending order
    heapq.heapify(happiness_ratings)
    
    # Extract the k largest ratings
    top_k = heapq.nlargest(k, happiness_ratings)
    
    # Create a min-heap to keep track of the smallest elements in each combination
    heapq.heapify(top_k)
    
    # Iterate to find the l largest sums of k objects
    for _ in range(l):
        if heapq.nlargest(k, top_k)[0] == -1:
            print(-1)
        else:
            best_combinations = heapq.nlargest(k, top_k)
            print(best_combinations[0])
            heapq.heapreplace(top_k, best_combinations[1] if len(best_combinations) > 1 else -1)

if __name__ == "__main__":
    main()