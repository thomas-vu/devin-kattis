def count_changes(answer, alternatives):
    max_changes = float('inf')
    for alt in alternatives:
        changes = 0
        parts1 = answer.split(', ')
        parts2 = alt.split(', ')
        for i in range(len(parts1)):
            if parts1[i] != parts2[i]:
                changes += 1
        max_changes = min(max_changes, changes)
    return max_changes

def find_least_incongruous(question, alternatives):
    min_max_changes = float('inf')
    least_incongruous_answers = []
    for answer in alternatives:
        changes = count_changes(answer, alternatives)
        if changes < min_max_changes:
            min_max_changes = changes
            least_incongruous_answers = [answer]
        elif changes == min_max_changes:
            least_incongruous_answers.append(answer)
    return least_incongruous_answers

# Main function to execute the solution
def main():
    question = input()
    N = int(input())
    alternatives = [input().strip() for _ in range(N)]
    least_incongruous_answers = find_least_incongruous(question, alternatives)
    for answer in least_incongruous_answers:
        print(answer)

if __name__ == "__main__":
    main()