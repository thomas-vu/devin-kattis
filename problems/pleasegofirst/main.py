def calculate_waiting_time(queue):
    n = len(queue)
    time_saved = 0
    
    while True:
        changed = False
        for i in range(n - 1):
            if queue[i] != queue[i + 1]:
                time_saved += min(5, n - i - 1)
                queue = queue[:i] + queue[i + 1:]
                n -= 1
                changed = True
                break
        if not changed:
            break
    
    return time_saved

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        queue = input()
        result = calculate_waiting_time(queue)
        print(result)

if __name__ == "__main__":
    main()