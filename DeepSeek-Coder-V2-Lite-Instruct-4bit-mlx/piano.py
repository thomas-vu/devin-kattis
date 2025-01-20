def can_schedule(pianos, tuners, days):
    schedule = [0] * (days + 1)
    
    for b, e in pianos:
        for day in range(b, e + 1):
            schedule[day] += 1
    
    for day in range(1, days + 1):
        if schedule[day] > tuners * 2:
            return "serious trouble"
        if schedule[day] > tuners and day % 7 in [6, 0]:
            return "weekend work"
    return "fine"

def main():
    n = int(input())
    for _ in range(n):
        m, p = map(int, input().split())
        pianos = [tuple(map(int, input().split())) for _ in range(m)]
        result = can_schedule(pianos, p, 100)
        print(result)

if __name__ == "__main__":
    main()