from collections import Counter, deque
import sys

def rearrange_string(s):
    count = Counter(s)
    max_heap = [(-value, char) for char, value in count.items()]
    heapq.heapify(max_heap)
    
    if any(-value > (len(s) - (-value)) / 2 for value, _ in max_heap):
        return "-1"
    
    q = deque()
    result = []
    
    while max_heap:
        neg_freq, char = heapq.heappop(max_heap)
        result.append(char)
        q.append((neg_freq + 1, char))
        
        if len(q) >= 2:
            heapq.heappush(max_heap, q.popleft())
    
    return "".join(result)

# Read input
s = sys.stdin.readline().strip()

# Rearrange the string and print the result
print(rearrange_string(s))