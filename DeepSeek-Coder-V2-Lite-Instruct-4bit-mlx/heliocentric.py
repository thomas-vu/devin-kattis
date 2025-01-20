import sys

def find_sync_day(e, m):
    earth_days = 365
    mars_days = 687
    day = 0
    
    while True:
        if day % earth_days == e and day % mars_days == m:
            return day
        day += 1

def main():
    test_cases = []
    for line in sys.stdin:
        e, m = map(int, line.split())
        test_cases.append((e, m))
        if len(test_cases) == 10:
            break
    
    for i, (e, m) in enumerate(test_cases):
        sync_day = find_sync_day(e, m)
        print(f"Case {i + 1}: {sync_day}")

if __name__ == "__main__":
    main()