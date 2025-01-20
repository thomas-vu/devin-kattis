def adjust_time(hh, mm):
    hh = int(hh)
    mm = int(mm)
    
    # Helper function to adjust a single digit
    def adjust_digit(d):
        if d == '0':
            return '9'
        else:
            return str(int(d) - 1)
    
    # Adjust hours and minutes
    if mm == 59:
        mm = '00'
        hh += 1
    else:
        mm = str(mm + 1).zfill(2)
    
    if hh == 24:
        hh = '00'
    
    return hh, mm

def generate_times(original_time):
    original_hh, original_mm = original_time.split(':')
    times = set()
    
    # Generate all possible valid times by adjusting each digit once
    for i in range(4):
        for j in [-1, 1]:
            if i < 2:  # Adjust hours
                hh = original_hh[:i] + adjust_digit(original_hh[i]) + original_hh[i+1:]
                mm = original_mm
            else:  # Adjust minutes
                hh = original_hh
                mm = original_mm[:i-2] + adjust_digit(original_mm[i-2]) + original_mm[i-1:]
            
            try:
                new_hh = int(hh)
                new_mm = int(mm)
                if 0 <= new_hh < 24 and 0 <= new_mm < 60:
                    times.add((hh, mm))
            except ValueError:
                continue
    
    return times

# Main function to solve the problem
def main():
    original_time = input().strip()
    current_time = input().strip()
    
    times = generate_times(current_time)
    
    # Sort the valid times and add the original time
    sorted_times = sorted(list(times) + [tuple(original_time.split(':'))])
    
    # Output the results
    print(len(sorted_times))
    for time in sorted_times:
        print(':'.join(time))

# Run the main function
if __name__ == "__main__":
    main()