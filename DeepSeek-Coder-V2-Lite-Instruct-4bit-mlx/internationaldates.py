def determine_date_format(date):
    parts = date.split('/')
    if len(parts[0]) == 2 and len(parts[1]) == 2:
        return "either"
    elif len(parts[0]) == 2 and len(parts[1]) == 4:
        return "US"
    elif len(parts[0]) == 4 and len(parts[1]) == 2:
        return "EU"
    else:
        return "either"

# Read input and output the result
date = input()
result = determine_date_format(date)
print(result)