def determine_drive_outcome(plays):
    start_position = -20  # Starting position is at the 20-yard line
    final_position = start_position + sum(plays)
    
    if final_position >= 80:
        return "Touchdown"
    elif final_position <= -20:
        return "Safety"
    else:
        return "Nothing"

# Read the number of plays
N = int(input())
# Read the yards gained or lost on each play
plays = list(map(int, input().split()))
# Determine the outcome of the drive
outcome = determine_drive_outcome(plays)
# Output the result
print(outcome)