def count_days_with_free_food():
    N = int(input())
    days_with_food = set()
    
    for _ in range(N):
        s, t = map(int, input().split())
        for day in range(s, t + 1):
            days_with_food.add(day)
    
    return len(days_with_food)

# Read the number of events from standard input
N = int(input())
for _ in range(N):
    s, t = map(int, input().split())
    
# Output the result
print(count_days_with_free_food())