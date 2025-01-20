def min_sprinklers(n, l, w, sprinklers):
    # Transform the problem into a 1D interval cover problem
    intervals = []
    for x, r in sprinklers:
        if r * 2 > w:
            left = max(0, x - (r**2 - ((w / 2)**2))**0.5)
            right = min(l, x + (r**2 - ((w / 2)**2))**0.5)
            intervals.append((left, right))
    
    # Sort the intervals by their starting points
    intervals.sort(key=lambda x: (x[0], -x[1]))
    
    # Use a greedy algorithm to cover the entire strip
    count = 0
    current_end = 0
    i = 0
    while current_end < l:
        max_end = -1
        while i < len(intervals) and intervals[i][0] <= current_end:
            max_end = max(max_end, intervals[i][1])
            i += 1
        
        if max_end <= current_end:
            return -1
        
        count += 1
        current_end = max_end
    
    return count

def main():
    while True:
        try:
            n, l, w = map(int, input().split())
            sprinklers = [tuple(map(int, input().split())) for _ in range(n)]
            result = min_sprinklers(n, l, w, sprinklers)
            print(result)
        except EOFError:
            break

if __name__ == "__main__":
    main()