def solve(N, ring):
    original = [0] * N
    
    # The sum of the first three elements in the ring is equal to the second element
    original[1] = (ring[0] + ring[1] + ring[2]) - ring[3]
    
    # The sum of the first three elements in the original ring is equal to the second element
    original[0] = (ring[1] + ring[2] + original[1]) - ring[0]
    
    # The sum of the first three elements in the original ring is equal to the second element
    original[2] = (ring[0] + ring[1] + original[1]) - ring[2]
    
    # The rest of the elements in the original ring can be deduced by adding each number and its two neighbors
    for i in range(3, N):
        original[i] = (ring[i - 1] + ring[i - 2] + original[i - 3]) - ring[i]
    
    # Output the original ring
    for num in original:
        print(num)

# Read input from stdin
N = int(input())
ring = [int(input()) for _ in range(N)]
solve(N, ring)