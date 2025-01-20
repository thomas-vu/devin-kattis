import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = [int(sys.stdin.readline().strip()) for _ in range(n)]
    
    # Create a list to store the result permutation
    b = [0] * n
    
    # Create a list to keep track of used indices
    used = [False] * n
    
    # Iterate through each element in the sequence
    for i in range(n):
        if not used[i]:
            # Find the position where b_i & a_i = 0
            for j in range(n):
                if (a[i] & a[j]) == 0 and not used[j]:
                    b[i] = a[j]
                    used[j] = True
                    break
    
    # Output the result permutation
    for bi in b:
        print(bi)

if __name__ == "__main__":
    main()