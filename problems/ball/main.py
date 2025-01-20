def find_added_pair(n, pairs):
    attendance = set()
    for pair in pairs:
        attendance.add(pair[0])
        attendance.add(pair[1])
    
    for pair in pairs:
        if (n - sum(attendance)) == 2 * pair[0]:
            return f"{pair[0]} {pair[1]}"
        if (n - sum(attendance)) == 2 * pair[1]:
            return f"{pair[1]} {pair[0]}"

n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n // 2 + 1)]
print(find_added_pair(n, pairs))