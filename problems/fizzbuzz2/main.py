def fizzbuzz(n, m, outputs):
    correct_outputs = [str(i) for i in range(1, m+1)]
    max_correct = 0
    best_candidate = -1
    
    for i in range(n):
        candidate_outputs = outputs[i]
        correct_count = 0
        
        for j in range(m):
            if candidate_outputs[j] == correct_outputs[j]:
                correct_count += 1
        
        if correct_count > max_correct:
            max_correct = correct_count
            best_candidate = i + 1
        elif correct_count == max_correct:
            best_candidate = min(best_candidate, i + 1)
    
    return best_candidate

# Read input
N, M = map(int, input().split())
outputs = [input().split() for _ in range(N)]

# Find the best candidate
result = fizzbuzz(N, M, outputs)
print(result)