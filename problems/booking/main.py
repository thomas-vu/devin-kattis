def min_rooms(bookings, cleaning_time):
    from collections import defaultdict
    
    events = []
    for code, start, end in bookings:
        start_time = int(start[:4] + start[5:7] + start[8:10] + start[11:13] + start[14:])
        end_time = int(end[:4] + end[5:7] + end[8:10] + end[11:13] + end[14:])
        events.append((start_time, 's'))
        events.append((end_time + cleaning_time, 'e'))
    
    events.sort()
    
    max_rooms = 0
    current_rooms = 0
    
    for event in events:
        if event[1] == 's':
            current_rooms += 1
            max_rooms = max(max_rooms, current_rooms)
        else:
            current_rooms -= 1
    
    return max_rooms

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        B = int(data[index])
        C = int(data[index + 1])
        index += 2
        bookings = []
        for _ in range(B):
            code = data[index]
            start_date = data[index + 1]
            end_date = data[index + 2]
            bookings.append((code, start_date, end_date))
            index += 3
        min_rooms_needed = min_rooms(bookings, C)
        results.append(min_rooms_needed)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()