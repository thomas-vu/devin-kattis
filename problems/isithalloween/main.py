def is_halloween(date):
    month, day = date.split()
    if (month == "OCT" and day == "31") or (month == "DEC" and day == "25"):
        return "yup"
    else:
        return "nope"

# Read input from stdin
date = input().strip()
print(is_halloween(date))