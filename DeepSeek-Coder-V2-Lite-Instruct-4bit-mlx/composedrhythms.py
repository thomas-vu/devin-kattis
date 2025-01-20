def decompose_rhythm(N):
    decomposition = []
    
    while N > 0:
        if N % 2 == 0:
            decomposition.append(2)
            N -= 2
        else:
            decomposition.append(3)
            N -= 3
    
    return decomposition

# Read input
N = int(input())

# Decompose the rhythm
decomposition = decompose_rhythm(N)

# Output the result
print(len(decomposition))
print(" ".join(map(str, decomposition)))