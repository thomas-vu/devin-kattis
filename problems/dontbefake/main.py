def read_input():
    N = int(input())
    friends = []
    for _ in range(N):
        line = input().split()
        M = int(line[0])
        intervals = list(map(int, line[1:]))
        friend_intervals = []
        for i in range(0, len(intervals), 2):
            friend_intervals.append([intervals[i], intervals[i+1]])
        friends.append(friend_intervals)
    return N, friends

def count_available_pictures(friends):
    max_pics = 0
    total_seconds = 0
    for second in range(86400):
        count = sum(1 for friend_intervals in friends if any(l <= second < r for l, r in friend_intervals))
        if count > max_pics:
            max_pics = count
            total_seconds = 1
        elif count == max_pics:
            total_seconds += 1
    return max_pics, total_seconds

N, friends = read_input()
max_pics, total_seconds = count_available_pictures(friends)
print(max_pics)
print(total_seconds)