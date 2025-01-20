def max_friends(n, k):
    events = []
    for _ in range(n):
        a_i, b_i = map(int, input().split())
        events.append((a_i, 'enter'))
        events.append((b_i + k, 'leave'))
    
    events.sort()
    
    current_friends = 0
    max_friends_count = 0
    
    for event in events:
        if event[1] == 'enter':
            current_friends += 1
            max_friends_count = max(max_friends_count, current_friends)
        else:
            current_friends -= 1
    
    return max_friends_count

n, k = map(int, input().split())
print(max_friends(n, k))