def determine_eligibility(name, start_date, birth_date, courses):
    # Convert dates to datetime objects for easier comparison
    from datetime import datetime
    start_date = datetime.strptime(start_date, "%Y/%m/%d")
    birth_date = datetime.strptime(birth_date, "%Y/%m/%d")
    
    # Check if the student began post-secondary studies in 2010 or later
    if start_date.year >= 2010:
        return "eligible"
    
    # Check if the student was born in 1991 or later
    if birth_date.year >= 1991:
        return "eligible"
    
    # Check if the student has completed more than 8 semesters of full-time study
    if courses >= (8 * 5):
        return "ineligible"
    
    # If none of the above applies, the student requires a coach petition
    return "coach petitions"

# Read number of cases
num_cases = int(input())

# Process each case
for _ in range(num_cases):
    name, start_date, birth_date, courses = input().split()
    courses = int(courses)
    result = determine_eligibility(name, start_date, birth_date, courses)
    print(f"{name} {result}")