def check_watering_schedule(w, p, t, b, r):
    # Calculate the total water provided by one complete cycle
    total_water_per_cycle = r * t + (r * b)
    
    # Check if the current watering schedule complies with the new regulation
    cycles_per_inspection = (t + b) // p
    total_water_provided = cycles_per_inspection * (r * t)
    
    # Check the remaining water after full cycles but before the next inspection
    remaining_time = (cycles_per_inspection * p) % (t + b)
    if remaining_time <= t:
        total_water_provided += (r * min(remaining_time, t))
    
    # Check if the total water provided meets the requirement per inspection
    return "The CSHOA decrees are as murky as the Forest Spirit" if total_water_provided < w else "Soot Sprites sing a lullaby"

# Read input
w, p, t, b, r = map(int, input().split())

# Output the result
print(check_watering_schedule(w, p, t, b, r))