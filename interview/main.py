import sys

input_data = sys.stdin.read().strip().split()
A, B, T, ta, tb = map(int, input_data[0:5])
C = int(input_data[5])
pairs = list(map(int, input_data[6:]))

companies = [(pairs[2*i], pairs[2*i+1]) for i in range(C)]
companies.sort(key=lambda x: x[0])  # sort by a_i ascending

def can_achieve(k):
    if k == 0:
        return True
    
    import heapq
    # We'll keep a max-heap for the k smallest b_i values seen so far.
    # Python's heapq is a min-heap, so we insert negative values to simulate a max-heap.
    heap = []
    
    for (a_i, b_i) in companies:
        if len(heap) < k:
            # Just push the negative b_i
            heapq.heappush(heap, -b_i)
        else:
            # If we already have k elements and the current b_i is smaller than the largest chosen (i.e., -heap[0]),
            # then replace it.
            largest_chosen_b = -heap[0]  # largest b in the chosen k (because of negation)
            if b_i < largest_chosen_b:
                # pop largest and insert current b_i
                heapq.heapreplace(heap, -b_i)
        
        if len(heap) == k:
            # Check feasibility
            max_b_chosen = -heap[0]
            A_needed = a_i
            B_needed = max_b_chosen
            
            time_spent = 0
            if A_needed > A:
                time_spent += (A_needed - A)*ta
            if B_needed > B:
                time_spent += (B_needed - B)*tb
            
            if time_spent <= T:
                return True
    
    return False

# Binary search for the maximum k
low, high = 0, C
answer = 0
while low <= high:
    mid = (low + high) // 2
    if can_achieve(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
