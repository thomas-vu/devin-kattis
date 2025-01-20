def min_avg_wait_time(test_cases):
    results = []
    for case in test_cases:
        N = case[0]
        customers = case[1:]
        # Sort the wood pieces by size to minimize waiting time
        for customer in customers:
            customer[1].sort()
        
        total_wait_time = 0
        for customer in customers:
            current_wait_time = 0
            for i, wood_size in enumerate(customer[1]):
                total_wait_time += current_wait_time + wood_size
                current_wait_time += wood_size
        
        avg_wait_time = total_wait_time / N
        results.append(avg_wait_time)
    return results

# Read input
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    wood_pieces = []
    for _ in range(N):
        data = list(map(int, input().split()))
        wood_pieces.append(data)
    test_cases.append((N, wood_pieces))

# Calculate and print results
results = min_avg_wait_time(test_cases)
for result in results:
    print("{:.10f}".format(result))