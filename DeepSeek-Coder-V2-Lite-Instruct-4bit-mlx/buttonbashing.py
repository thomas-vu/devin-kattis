def min_button_presses(buttons, target):
    # Initialize a list to store the minimum presses for each time from 0 to 3600
    min_presses = [float('inf')] * (3600 + 1)
    min_presses[0] = 0  # Base case: 0 presses to achieve 0 seconds
    
    for time in range(1, 3601):
        for button_value in buttons:
            if time - button_value >= 0 and min_presses[time - button_value] + 1 < min_presses[time]:
                min_presses[time] = min_presses[time - button_value] + 1
    
    # Find the minimum presses to reach or exceed the target time
    min_presses_target = float('inf')
    extra_seconds = 0
    
    for time in range(target, 3601):
        if min_presses[time] != float('inf'):
            if min_presses[time] < min_presses_target:
                min_presses_target = min_presses[time]
                extra_seconds = time - target
            break
    
    if min_presses_target == float('inf'):
        # If we didn't find a direct match, find the smallest achievable time above the target
        min_presses_target = float('inf')
        extra_seconds = 0
        for time in range(target, -1, -1):
            if min_presses[time] != float('inf'):
                min_presses_target = min_presses[time]
                extra_seconds = target - time
                break
    
    return min_presses_target, extra_seconds

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        t = int(data[index + 1])
        buttons = list(map(int, data[index + 2: index + 2 + n]))
        index += 2 + n
        min_presses, extra_seconds = min_button_presses(buttons, t)
        results.append((min_presses, extra_seconds))
    
    for result in results:
        print(result[0], result[1])

if __name__ == "__main__":
    main()