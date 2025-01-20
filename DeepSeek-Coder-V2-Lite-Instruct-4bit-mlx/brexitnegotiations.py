import heapq

def calculate_longest_meeting(n, topics):
    # Create a list to store the minimum time required for each topic
    min_time = [0] * (n + 1)
    
    # Create a list to store the number of dependencies for each topic
    dep_count = [0] * (n + 1)
    
    # Create a list to store the adjacency list for each topic
    adj_list = [[] for _ in range(n + 1)]
    
    # Build the adjacency list and count dependencies for each topic
    for i in range(1, n + 1):
        e_i, d_i = topics[i - 1]
        dep_count[i] = d_i
        for b in topics[i - 1][2:]:
            adj_list[b].append(i)
    
    # Create a priority queue to process topics with no dependencies first
    pq = []
    
    # Initialize the priority queue with topics that have no dependencies
    for i in range(1, n + 1):
        if dep_count[i] == 0:
            heapq.heappush(pq, (topics[i - 1][0], i))
    
    # Process the topics with dependencies using a topological sort-like approach
    while pq:
        time, topic = heapq.heappop(pq)
        for neighbor in adj_list[topic]:
            dep_count[neighbor] -= 1
            if dep_count[neighbor] == 0:
                heapq.heappush(pq, (time + topics[neighbor - 1][0], neighbor))
        min_time[topic] = time
    
    # The longest meeting time will be the maximum value in min_time minus the initial recap minutes
    return max(min_time[1:])

# Read input
n = int(input().strip())
topics = [list(map(int, input().strip().split())) for _ in range(n)]

# Calculate and output the minimum possible length of the longest meeting
result = calculate_longest_meeting(n, topics)
print(result)