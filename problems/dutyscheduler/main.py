def main():
    import sys
    input = sys.stdin.readline
    
    m, n = map(int, input().split())
    ras = []
    
    for _ in range(m):
        name, days_str = input().split()
        days = list(map(int, days_str.split()))
        ras.append((name, days))
    
    # Create a list to store the assignments for each day
    assignments = [None] * n
    
    # Assign RAs to days based on availability
    for ra in ras:
        name, available_days = ra
        for day in available_days:
            if assignments[day - 1] is None:
                assignments[day - 1] = [name]
            else:
                assignments[day - 1].append(name)
    
    # Find the maximum number of days any RA is assigned
    max_days = 0
    for assignment in assignments:
        if assignment is not None:
            max_days = max(max_days, len(assignment))
    
    # Output the result
    print(max_days)
    for i, assignment in enumerate(assignments):
        if assignment is not None:
            print(f"Day {i + 1}:", " ".join(sorted(assignment)))

if __name__ == "__main__":
    main()