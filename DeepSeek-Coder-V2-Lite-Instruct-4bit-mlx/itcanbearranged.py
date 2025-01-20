def min_rooms(N, M, courses, cleaning_times):
    from heapq import heappush, heappop
    
    # Create a list to store the end times of each room
    rooms = []
    
    # Sort courses by their starting time
    sorted_courses = sorted([(A, B, S, i) for i in range(N)], key=lambda x: x[0])
    
    # Iterate through each course to assign it to a room
    for start, end, students, index in sorted_courses:
        # Check if there is a room available with enough capacity
        while rooms and rooms[0] <= start:
            heappop(rooms)
        
        # Assign the course to a room
        if students <= M:
            heappush(rooms, end + cleaning_times[index][index])
    
    return len(rooms)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for t in range(T):
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        
        courses = []
        for i in range(N):
            A = int(data[index])
            B = int(data[index + 1])
            S = int(data[index + 2])
            courses.append((A, B, S))
            index += 3
        
        cleaning_times = []
        for i in range(N):
            row = list(map(int, data[index: index + N]))
            cleaning_times.append(row)
            index += N
        
        result = min_rooms(N, M, courses, cleaning_times)
        results.append(f"Case {t + 1}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()