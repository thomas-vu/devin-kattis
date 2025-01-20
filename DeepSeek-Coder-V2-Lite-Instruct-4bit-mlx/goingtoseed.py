import sys

def main():
    N = int(sys.stdin.readline().strip())
    
    # Initialize the search space and the last observed positions
    left, right = 1, N
    
    # Perform binary search to find the position of the Great Seedling
    for _ in range(16):
        mid = (left + right) // 2
        
        # Ask Applejack and Apple Bloom to observe the trees
        print(f"Q {left} {mid} {mid+1} {right}")
        sys.stdout.flush()
        
        # Read the responses from Applejack and Apple Bloom
        w1, w2 = map(int, sys.stdin.readline().strip().split())
        
        if w1 == 1 and w2 == 1:
            right = mid
        else:
            left = mid + 1
    
    # Guess the position of the Great Seedling
    print(f"A {left}")
    sys.stdout.flush()

if __name__ == "__main__":
    main()