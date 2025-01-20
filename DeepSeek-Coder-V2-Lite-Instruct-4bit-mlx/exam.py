def max_possible_score(k, answers_you, answers_friend):
    correct_count = 0
    
    for i in range(len(answers_you)):
        if answers_you[i] == 'T' and answers_friend[i] == 'T':
            correct_count += 1
        elif answers_you[i] == 'F' and answers_friend[i] == 'F':
            correct_count += 1
    
    max_correct = min(k, len(answers_you)) + correct_count - k
    return max_correct

# Read input from stdin
k = int(input())
answers_you = input()
answers_friend = input()

# Compute and print the result
print(max_possible_score(k, answers_you, answers_friend))