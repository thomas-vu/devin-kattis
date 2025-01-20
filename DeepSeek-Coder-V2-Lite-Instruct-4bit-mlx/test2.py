def find_sets(answers):
    activities = set()
    for answer in answers:
        _, *choices, chosen = answer.split()
        activities.add(chosen)
    
    sets = []
    while activities:
        activity = min(activities)
        activities.remove(activity)
        current_set = {activity}
        to_remove = set()
        for other in activities:
            if all(other not in preferences[activity] for activity, preferences in answers.items()):
                current_set.add(other)
                to_remove.add(other)
        for rem in to_remove:
            activities.remove(rem)
        sets.append(sorted(current_set))
    
    return sorted([sorted(s) for s in sets], key=lambda x: x[0])

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        answers = {}
        for _ in range(n):
            question = input().split()
            answers[question[0]] = [x for x in question[1:6]], question[5]
        sets = find_sets(answers)
        for s in sets:
            print(', '.join(s))

if __name__ == "__main__":
    main()