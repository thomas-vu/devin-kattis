def can_manipulate(N, points, matches):
    # Calculate the minimum points needed to win
    min_points = 2 * (sum(points) - points[N-1]) + 1
    
    # Calculate the total points for each team if they win all remaining matches
    future_points = [p + (matches[i][0] != N) * 2 + (matches[i][1] != N) for i, p in enumerate(points)]
    
    # Check if it's possible to achieve the minimum points and have more than any other team
    max_other_points = max([p for i, p in enumerate(future_points) if i != N-1])
    
    # Check the conditions
    return future_points[N-1] > max_other_points, min_points

def manipulate_matches(N, points, matches):
    # Check if it's possible to manipulate the matches
    can_win, min_points = can_manipulate(N, points, matches)
    if not can_win:
        return "NO"
    
    # Manipulate the matches to ensure victory
    results = []
    for match in matches:
        if points[match[0]-1] > points[match[1]-1]:
            results.append(2)  # Team N wins against the other team in the match
        elif points[match[0]-1] < points[match[1]-1]:
            results.append(0)  # Team N loses to the other team in the match
        else:
            results.append(1)  # Draw, no change in points for Team N
    
    return results

while True:
    input_line = list(map(int, input().split()))
    if input_line[0] == -1:
        break
    
    N = input_line[0]
    M = input_line[1]
    points = list(map(int, input().split()))
    matches = [tuple(map(int, input().split())) for _ in range(M)]
    input()  # Consume the blank line
    
    result = manipulate_matches(N, points, matches)
    if result == "NO":
        print("NO")
    else:
        print(' '.join(map(str, result)))