def count_adjustments(preferences):
    up = 0
    down = 0
    adjustments = 0
    
    for pref in preferences:
        if pref == 'U':
            adjustments += 1
            up = max(0, up - 1)
            down = max(0, down + 1)
        else:
            adjustments += 1
            up = max(0, up + 1)
            down = max(0, down - 1)
    
    return adjustments, up, down

def main():
    preferences = input().strip()
    n = len(preferences)
    
    # Policy 1: Always leave the seat up when leaving
    total_adjustments, _, _ = count_adjustments(preferences)
    print(total_adjustments)
    
    # Policy 2: Always leave the seat down when leaving
    total_adjustments, _, _ = count_adjustments(preferences)
    print(total_adjustments)
    
    # Policy 3: Leave the seat as you would like to find it
    total_adjustments, up, down = count_adjustments(preferences)
    print(total_adjustments - min(up, down))

if __name__ == "__main__":
    main()