import datetime

# Function to determine the day of the week for a given date in 2009
def get_day_of_week(d, m):
    # Create a date object for the given day and month in 2009
    date_in_2009 = datetime.date(2009, m, d)
    # Get the day of the week as an integer (Monday is 0, ..., Sunday is 6)
    day_of_week = date_in_2009.weekday()
    # Map the integer to the corresponding day of the week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # Return the day of the week as a string
    return days[day_of_week]

# Read input from the user
D, M = map(int, input().split())
# Get and print the day of the week
print(get_day_of_week(D, M))