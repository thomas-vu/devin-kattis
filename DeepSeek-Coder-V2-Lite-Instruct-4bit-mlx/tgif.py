def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month == 'JAN': return 31
    elif month == 'FEB': return 29 if is_leap_year(year) else 28
    elif month == 'MAR': return 31
    elif month == 'APR': return 30
    elif month == 'MAY': return 31
    elif month == 'JUN': return 30
    elif month == 'JUL': return 31
    elif month == 'AUG': return 31
    elif month == 'SEP': return 30
    elif month == 'OCT': return 31
    elif month == 'NOV': return 30
    else: return 31 # DEC

def day_of_year(day, month, year):
    days = 0
    for m in range(1, int(month[:3])):
        days += days_in_month(year, m)
    return days + day - 1

def calculate_day(day, month, year):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day_index = days.index('MON') + day_of_year(day, month, year) % 7
    return days[day_index % 7]

def main():
    date, day = input().split()
    day_of_week = calculate_day(int(date.split()[0]), date.split()[1], 2024)
    print('TGIF' if day_of_week == 'FRI' else 'not sure' if is_leap_year(2024) and day == 'FEB' else ':(')

main()