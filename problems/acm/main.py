def calculate_score(log):
    problems = {}
    penalties = {}
    
    for entry in log:
        minutes, problem, result = entry.split()
        minutes = int(minutes)
        
        if problem not in problems:
            problems[problem] = []
            penalties[problem] = 0
        
        if result == 'right':
            problems[problem].append(minutes)
        else:
            penalties[problem] += 20
    
    total_time = 0
    problems_solved = 0
    
    for problem, times in problems.items():
        if len(times) > 0:
            problems_solved += 1
            total_time += min(times) + penalties[problem] * len(times)
    
    return problems_solved, total_time

log = []
while True:
    entry = input()
    if entry == '-1':
        break
    log.append(entry)

problems_solved, total_time = calculate_score(log)
print(f"{problems_solved} {total_time}")