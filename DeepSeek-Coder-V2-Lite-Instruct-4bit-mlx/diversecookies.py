def max_cookies(N, A, B, C):
    # The maximum number of cookies that can be distributed is limited by the smallest group size among Alf, Beata, and their friends
    min_group = min(A // (N - 1), B // (N - 1), C // (N - 1))
    # If the minimum group size is less than or equal to 2, we can distribute up to N * (N - 1) cookies
    if min_group <= 2:
        return N * (N - 1)
    # Otherwise, we distribute the cookies in a way that avoids eating the same kind of cookie twice in a row
    else:
        return A + B + C - 3 * (N - 1)

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()
N, A, B, C = int(data[0]), int(data[1]), int(data[2]), int(data[3])

# Output the result
print(max_cookies(N, A, B, C))