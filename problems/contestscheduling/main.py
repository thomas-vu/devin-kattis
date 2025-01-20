import sys
from datetime import datetime, timedelta

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 0

def next_friday(date):
    while True:
        if date.weekday() == 4:  # Friday
            return date
        date += timedelta(days=1)

def calculate_surprise_penalty(initial_date, scheduled_dates):
    penalty = 0
    for i, date in enumerate(scheduled_dates):
        if initial_date != date:
            penalty += (date - initial_date).days ** 2
        initial_date = date
    return penalty

def main():
    Z = int(sys.stdin.readline().strip())
    F = int(sys.stdin.readline().strip())
    forbidden_dates = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(F)]
    
    # Convert forbidden dates to datetime objects
    forbidden_dates = [(datetime(y, 10, d),) for y, _, d in forbidden_dates]
    
    # Calculate the initial date of contest
    start_date = datetime(2018, 10, 274)
    
    # Schedule the contest for Z years
    scheduled_dates = []
    current_date = start_date
    
    for _ in range(Z):
        while True:
            next_date = next_friday(current_date)
            if not any(datetime(y, 10, d) == next_date for y, _, d in forbidden_dates):
                scheduled_dates.append(next_date)
                current_date = next_date + timedelta(days=7)
                break
    
    # Calculate the total surprise penalty
    total_penalty = calculate_surprise_penalty(datetime(2018, 10, 12), scheduled_dates)
    
    # Output the result
    print(total_penalty)
    for date in scheduled_dates:
        print(f"{date.year} 10 {date.day}")

if __name__ == "__main__":
    main()