def read_ints():
    return list(map(int, input().split()))

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = read_ints()
    
    min_heap = []  # For the larger half of A
    max_heap = []  # For the smaller half of A
    medians = []
    
    for i in range(N):
        num = A[i]
        
        if not min_heap or num <= -max_heap[0]:
            heappush(max_heap, -num)
        else:
            heappush(min_heap, num)
        
        # Balance the heaps
        if len(max_heap) > len(min_heap) + 1:
            heappush(min_heap, -heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))
        
        # Calculate the median
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) // 2
        else:
            median = -max_heap[0]
        
        medians.append(median)
    
    print(sum(medians))