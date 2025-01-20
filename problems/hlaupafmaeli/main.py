def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def gunna_birthday(year):
    if is_leap_year(year):
        return 29
    else:
        return 'Neibb'

# Read the input from stdin
year = int(input().strip())
print(gunna_birthday(year))