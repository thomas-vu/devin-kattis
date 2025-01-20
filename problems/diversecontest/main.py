from itertools import combinations

def count_distinct_contests(n, k, problems):
    topics = set()
    for problem in problems:
        topics.update(problem[1:])
    
    topic_combinations = list(combinations(topics, k))
    contests = set()
    
    for combo in topic_combinations:
        valid = True
        for problem in problems:
            count = sum(1 for topic in combo if topic in problem[1:])
            if count > (len(problem) - 1) / 2:
                valid = False
                break
        if valid:
            contests.add(tuple(sorted([problem[0] for problem in problems if all(topic in problem[1:] for topic in combo)])))
    
    return len(contests)

# Read input
n, k = map(int, input().split())
problems = [input().split() for _ in range(n)]
for i in range(len(problems)):
    problems[i][0] = int(problems[i][0])

# Output the result
print(count_distinct_contests(n, k, problems))