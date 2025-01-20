def has_optimal_launch_window(year):
    # Optimal launch windows occur once every 26 months.
    # Convert months to years: 26 months = 26 / 12 years approximately.
    interval_in_years = 26 / 12
    
    # Calculate the first window in April 2018.
    start_year = 2018
    start_month = 4
    
    # Check each window in the given year.
    while True:
        if (start_year + start_month / 12) == year:
            return "yes"
        # Move to the next window.
        start_month += 2
        if start_month >= 12:
            start_month = 0
            start_year += 1
        if start_year > year:
            break
    return "no"

# Read the input year.
y = int(input())
print(has_optimal_launch_window(y))