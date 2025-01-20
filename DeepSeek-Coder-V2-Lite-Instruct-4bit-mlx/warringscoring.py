def main():
    n = int(input())
    points = [input().strip() for _ in range(n)]
    
    # Notnomde's system: longest streak of points
    streak_count = 0
    max_streak = 0
    for point in points:
        if point == 'Notnomde':
            streak_count += 1
            max_streak = max(max_streak, streak_count)
        else:  # Yraglac's point
            streak_count = 0
    
    notnomde_streak = max_streak
    
    # Yraglac's system: largest lead at a single point
    leads = []
    notnomde_score = 0
    yraglac_score = 0
    for i in range(n):
        if points[i] == 'Notnomde':
            notnomde_score += 1
        else:  # Yraglac's point
            yraglac_score += 1
        leads.append(yraglac_score - notnomde_score)
    
    max_lead = max(leads)
    yraglac_lead = max_lead
    
    # Determine the outcome based on both systems
    if notnomde_streak > yraglac_lead:
        print('Notnomde')
    elif yraglac_lead > notnomde_streak:
        print('Yraglac')
    else:
        print('Agree')

if __name__ == "__main__":
    main()