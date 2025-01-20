def min_seconds(S, P, A, B):
    target = (P + 1) // 2
    if S >= target:
        return 0
    
    # If creating a new problem is faster than solving one
    if B <= A:
        return (target - S) * B
    
    # If solving problems is faster than creating new ones
    min_solve = target - S
    extra_time = (min_solve * A) + ((P - min_solve) * B)
    return extra_time

# Read input
S = int(input())
P = int(input())
A = int(input())
B = int(input())

# Calculate and print the minimum number of seconds
print(min_seconds(S, P, A, B))