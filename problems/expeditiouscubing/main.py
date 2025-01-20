def can_win(t1, t2, t3, t4, target):
    times = [t1, t2, t3, t4]
    min_time = min(times)
    max_time = max(times)
    remaining_sum = sum(times) - min_time - max_time
    
    average_remaining = remaining_sum / 3
    if average_remaining <= target:
        return "infinite"
    
    worst_possible = 20 - min(max_time, target)
    return f"{worst_possible:.2f}"

def main():
    while True:
        try:
            t1, t2, t3, t4 = map(float, input().split())
            target = float(input())
        except EOFError:
            break
        
        result = can_win(t1, t2, t3, t4, target)
        print(result)

if __name__ == "__main__":
    main()