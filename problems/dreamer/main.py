from datetime import datetime, timedelta

def is_valid_date(day, month, year):
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False

def main():
    t = int(input())
    for _ in range(t):
        parts = input().split()
        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        possible_dates = set()
        
        for d in range(1, 32):
            for m in range(1, 13):
                if is_valid_date(d, m, year):
                    possible_dates.add((d, m, year))
        
        valid_count = 0
        earliest_date = datetime(2000, 1, 1)
        
        for d, m, y in possible_dates:
            if y > 2000 or (y == 2000 and m > 1) or (y == 2000 and m == 1 and d >= 1):
                valid_count += 1
                if (y, m, d) < earliest_date:
                    earliest_date = datetime(y, m, d)
        
        if valid_count == 0:
            print(0)
        else:
            print(valid_count, earliest_date.strftime('%d %m %Y'))

main()