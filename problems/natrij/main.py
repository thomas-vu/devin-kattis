def time_difference(current, explosion):
    # Convert current and explosion times to seconds
    h1, m1, s1 = map(int, current.split(':'))
    h2, m2, s2 = map(int, explosion.split(':'))
    
    current_seconds = h1 * 3600 + m1 * 60 + s1
    explosion_seconds = h2 * 3600 + m2 * 60 + s2
    
    # Calculate the difference in seconds
    if explosion_seconds >= current_seconds:
        time_to_explosion = explosion_seconds - current_seconds
    else:
        # Adjust for the next day
        time_to_explosion = (24 * 3600) - (current_seconds - explosion_seconds)
    
    # Convert the time to hh:mm:ss format
    hours = time_to_explosion // 3600
    minutes = (time_to_explosion % 3600) // 60
    seconds = time_to_explosion % 60
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Read input from stdin
current_time = input().strip()
explosion_time = input().strip()

# Calculate and print the result
print(time_difference(current_time, explosion_time))