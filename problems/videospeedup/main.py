def calculate_original_length(n, p, k, events):
    # Initialize the total time for the new video and the original speed factor
    total_time = 0.0
    original_speed_factor = (100 + p) / 100.0
    
    # Calculate the total time for each segment in the new video
    for i, event_time in enumerate(events):
        speed_factor = (100 + (i + 1) * p) / 100.0
        segment_length = (event_time - total_time) / speed_factor
        total_time += segment_length * speed_factor
    
    # The final segment length is the remaining time to k seconds
    final_segment_length = (k - total_time) / original_speed_factor
    total_time += final_segment_length * original_speed_factor
    
    return k if total_time >= k else (k * original_speed_factor)

# Read input
n, p, k = map(int, input().split())
events = list(map(int, input().split()))

# Calculate and output the original length of the video
original_length = calculate_original_length(n, p, k, events)
print("{:.6f}".format(original_length))