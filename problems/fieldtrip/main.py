def find_buses():
    N = int(input())
    sections = list(map(int, input().split()))
    
    # Check if the total number of students is divisible by 3, as each bus must have at least one student
    total_students = sum(sections)
    if total_students % 3 != 0:
        print(-1)
        return
    
    # Calculate the target number of students per bus
    capacity_per_bus = total_students // 3
    
    # Initialize variables to keep track of the number of students loaded into each bus and the last section assigned
    buses = [0, 0, 0]
    last_section = [0, 0, 0]
    
    # Iterate over the sections to load them into buses
    for i in range(N):
        # Assign students from the current section to the first available bus
        for k in range(3):
            if buses[k] < (i + 1) * capacity_per_bus:
                buses[k] += sections[i]
                last_section[k] = i + 1
                break
    
    # Check if we have achieved a teacher-free bus ride
    if buses[0] % capacity_per_bus == 0 and buses[1] % capacity_per_bus == 0 and buses[2] % capacity_per_bus == 0:
        print(last_section[0], last_section[1])
    else:
        print(-1)

# Call the function to find the buses
find_buses()