def find_scores(s, d):
    # Calculate the possible values for each team's score
    a = (s + d) / 2
    b = s - a
    
    # Check if both scores are non-negative integers
    if a < 0 or b < 0 or not a.is_integer() or not b.is_integer():
        return "impossible"
    
    # Return the scores, with the largest first
    if a >= b:
        return f"{int(a)} {int(b)}"
    else:
        return f"{int(b)} {int(a)}"

# Read number of test cases
n = int(input())
for _ in range(n):
    s, d = map(int, input().split())
    print(find_scores(s, d))