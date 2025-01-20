def main():
    n, k = map(int, input().split())
    names = input().split()
    comparisons = {}
    
    for _ in range(k):
        a, rel, b = input().split()
        if rel == '<':
            comparisons[b] = comparisons.get(b, set()) | {a}
        else:  # rel == '>'
            comparisons[a] = comparisons.get(a, set()) | {b}
    
    locked_names = {}
    for name in names:
        if name not in comparisons:
            locked_names[name] = []
    
    while locked_names:
        new_locked_names = {}
        for name in locked_names:
            solved_more = set()
            if name in comparisons:
                for other in comparisons[name]:
                    solved_more |= locked_names.get(other, set())
            if all(solved in solved_more for solved in locked_names[name]):
                for other in comparisons:
                    if name in comparisons[other]:
                        new_locked_names[other] = new_locked_names.get(other, set()) | {name}
            else:
                new_locked_names[name] = locked_names[name]
        locked_names = new_locked_names
    
    if len(locked_names) == n:
        sorted_names = sorted(locked_names.keys())
        print(' '.join(sorted_names))
    else:
        print('veit ekki')

if __name__ == "__main__":
    main()