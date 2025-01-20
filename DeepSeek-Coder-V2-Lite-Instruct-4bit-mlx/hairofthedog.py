def count_hangovers(days):
    hungover_count = 0
    consecutive_drinks = 0
    
    for day in days:
        if day == "drunk":
            consecutive_drinks += 1
        else:
            if consecutive_drinks > 0:
                hungover_count += 1
                consecutive_drinks = 0
    
    return hungover_count

# Read input
N = int(input())
days = [input().strip() for _ in range(N)]

# Count hangovers
result = count_hangovers(days)
print(result)