def calculate_points(issue_date, offenses):
    def date_to_days(date):
        year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
        return year * 365 + month * 30 + day
    
    def days_to_date(days):
        year = days // 365
        days %= 365
        month = days // 30
        day = days % 30
        return f"{year:04d}-{month:02d}-{day:02d}"
    
    issue_days = date_to_days(issue_date)
    merit, demerit = 0, 0
    points_history = []
    
    for offense in offenses:
        offense_days = date_to_days(offense[0])
        points = offense[1]
        
        while demerit > 2 * merit and merit > 0:
            demerit -= 2 * merit
            merit = max(0, merit - 2)
        
        while demerit > 0:
            reduction = min(demerit, max(1, demerit // 2))
            demerit -= reduction
            if reduction == int(reduction):
                points_history.append((days_to_date(offense_days), reduction))
        
        while demerit > 2 * merit and merit > 0:
            demerit -= 2 * merit
            merit = max(0, merit - 2)
        
        demerit += points
        while demerit > 0 and merit < 5:
            reduction = min(demerit, max(1, demerit // 2))
            demerit -= reduction
            merit += 1
            points_history.append((days_to_date(offense_days), reduction * -1))
        
        points_history.append((days_to_date(offense_days), points))
        
        if merit == 5:
            break
    
    while demerit > 0 and issue_days < offense_days:
        reduction = min(demerit, max(1, demerit // 2))
        demerit -= reduction
        issue_days += 183 if not is_leap_year(issue_days // 365) else 184
    
    return points_history

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def main():
    issue_date = input().strip()
    offenses = []
    while True:
        try:
            line = input().strip()
            if not line:
                break
            date, points = map(str, line.split())
            offenses.append((date, int(points)))
        except EOFError:
            break
    
    points_history = calculate_points(issue_date, offenses)
    for date, points in points_history:
        if points > 0:
            print(f"{date} {points} demerit point(s).")
        elif points < 0:
            print(f"{date} {abs(points)} merit point(s).")
        else:
            print(f"{date} No merit or demerit points.")

if __name__ == "__main__":
    main()