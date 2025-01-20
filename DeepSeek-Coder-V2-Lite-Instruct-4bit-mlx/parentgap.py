def is_leap_year(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def days_in_year(y):
    return 366 if is_leap_year(y) else 365

def calculate_parent_gap(y):
    # Mother's Day is the second Sunday in May
    may_first = 1 if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else 0
    may_days = 31 + may_first
    mothers_day = (15 - (may_days % 7)) % 7 + may_days
    
    # Father's Day is the third Sunday in June
    june_first = (7 - (may_days % 7)) % 7 + may_days
    fathers_day = june_first + 21 - 7
    
    parent_gap = (fathers_day - mothers_day) // 7
    return "6 weeks" if parent_gap == 6 else "5 weeks"

# Main function to take input and output the result
y = int(input())
print(f"{y} {calculate_parent_gap(y)}")