def find_largest_d(s):
    s = list(set(s))  # Remove duplicates and sort the set to make it easier to find combinations
    s.sort()
    
    n = len(s)
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            for k in range(j - 1, -1, -1):
                a, b, c = s[k], s[j], s[i]
                if a + b + c < s[-1]:  # Check if the sum is less than the largest element
                    continue
                for l in range(n):
                    if a + b + c == s[l]:  # Check if the sum equals an element in the set
                        continue
                    return a + b + c  # Return the largest sum found
    return "no solution"

# Read input
N = int(input())
S = [int(input()) for _ in range(N)]

# Output the result
print(find_largest_d(S))