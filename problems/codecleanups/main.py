def calculate_cleanup_phases(n, dirty_push_days):
    dirtiness = 0
    cleanup_phases = 0
    
    for day in dirty_push_days:
        dirtiness += day
        while dirtiness >= 20:
            cleanup_phases += 1
            # Perform cleanup phase, resetting dirtiness to zero
            for pushed_day in dirty_push_days:
                if pushed_day <= day:
                    dirtiness -= pushed_day
            # Recalculate the total dirtiness after cleanup phase
            if dirtiness < 20:
                break
    
    return cleanup_phases

# Read input
n = int(input())
dirty_push_days = list(map(int, input().split()))

# Calculate and output the result
print(calculate_cleanup_phases(n, dirty_push_days))