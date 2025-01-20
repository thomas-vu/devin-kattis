def minutes_waited(start, end):
    start_hour, start_minute = map(int, start.split(':'))
    end_hour, end_minute = map(int, end.split(':'))
    
    total_start_minutes = start_hour * 60 + start_minute
    total_end_minutes = end_hour * 60 + end_minute
    
    return total_end_minutes - total_start_minutes

# Sample Input 1
start_time = "02:02"
end_time = "20:20"
print(minutes_waited(start_time, end_time))  # Output: 1098

# Sample Input 2
start_time = "13:37"
end_time = "13:42"
print(minutes_waited(start_time, end_time))  # Output: 5

# Sample Input 3
start_time = "20:20"
end_time = "02:02"
print(minutes_waited(start_time, end_time))  # Output: 342