def can_reconstruct(n, p, times):
    from collections import defaultdict
    
    # Create a dictionary to count the number of problems solved by each team
    problem_count = defaultdict(int)
    
    # Count the number of problems solved by each team based on their time penalties
    for i in range(n):
        count = 0
        t = times[i]
        while t > 0:
            count += 1
            t //= p
        problem_count[times[i]] = count
    
    # Check for uniqueness of the number of problems solved by each team
    unique_counts = set(problem_count.values())
    
    # If the number of unique counts is equal to the number of teams, it's possible to reconstruct
    if len(unique_counts) == n:
        for i in range(n):
            print(problem_count[times[i]])
    else:
        print("ambiguous")

# Read input
n, p = map(int, input().split())
times = [int(input()) for _ in range(n)]

# Process the input and output the result
can_reconstruct(n, p, times)