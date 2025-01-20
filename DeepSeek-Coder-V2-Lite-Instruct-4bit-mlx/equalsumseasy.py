def find_subsets(S):
    n = len(S)
    total_sum = sum(S)
    
    # Check all possible subsets
    for mask in range(1, 1 << n):
        subset_sum = 0
        subset = []
        for i in range(n):
            if (mask & (1 << i)):
                subset_sum += S[i]
                subset.append(S[i])
        
        # Check if the sum of this subset is half of the total sum
        if subset_sum == (total_sum // 2) and subset_sum * 2 != total_sum:
            return subset
    
    return None

def main():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        S = list(map(int, input().split()))
        
        subsets = find_subsets(S)
        
        print("Case #{}:".format(t))
        if subsets is not None:
            print(" ".join(map(str, subsets)))
        else:
            print("Impossible")

if __name__ == "__main__":
    main()