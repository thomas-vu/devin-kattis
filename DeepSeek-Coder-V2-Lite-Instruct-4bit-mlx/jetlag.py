import sys

def can_participate(activities, n):
    # Sort activities by start time
    activities.sort()
    
    # Initialize variables for the sleep schedule
    sleep_schedule = []
    current_time = 0
    
    # Iterate through activities to plan sleep schedule
    for i in range(n):
        b_i, e_i = activities[i]
        
        # If current time is less than the start of the activity, sleep if possible
        if current_time < b_i:
            # Check the next multiple of 20 that is greater than or equal to current time
            k = ((current_time + 19) // 20) * 20
            if k < b_i:
                sleep_schedule.append((current_time, k))
                current_time = k + e_i
            else:
                return "impossible"
        else:
            # If current time is greater than or equal to the start of the activity, adjust sleep duration
            if current_time + 20 <= e_i:
                sleep_schedule.append((current_time, current_time + 20))
                current_time = e_i + (e_i - current_time)
            else:
                return "impossible"
    
    # Output the sleep schedule
    print(len(sleep_schedule))
    for s, t in sleep_schedule:
        print(s, t)

# Read input from stdin
n = int(input().strip())
activities = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Check if it's possible to participate in all activities
can_participate(activities, n)