import sys
from datetime import datetime, timedelta

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def parse_date(A, B, C):
    # Try all permutations of A, B, C to find the earliest valid date
    dates = [
        (int(A), int(B), int(C)),
        (int(A), int(C), int(B)),
        (int(B), int(A), int(C)),
        (int(B), int(C), int(A)),
        (int(C), int(A), int(B)),
        (int(C), int(B), int(A))
    ]
    
    for year, month, day in dates:
        try:
            if 2000 <= year <= 2999 and 1 <= month <= 12 and 1 <= day <= (31 if month in [1, 3, 5, 7, 8, 10, 12] else (30 if month in [4, 6, 9, 11] else (29 if is_leap_year(year) else 28))):
                return datetime(year, month, day).strftime('%Y-%m-%d')
        except ValueError:
            continue
    return None

# Read input from stdin
input_line = sys.stdin.readline().strip()
A, B, C = input_line.split('/')

# Parse the date components
A = A.lstrip('0') if A.isdigit() else A
B = B.lstrip('0') if B.isdigit() else B
C = C.lstrip('0') if C.isdigit() else C

# Convert year components to full years
if len(A) == 2:
    A = int(A) + 2000 if A.isdigit() else int(A)
if len(C) == 2:
    C = int(C) + 2000 if C.isdigit() else int(C)

# Parse the date and handle illegal dates
result = parse_date(A, B, C)
if result:
    print(result)
else:
    print(f"{input_line} is illegal")