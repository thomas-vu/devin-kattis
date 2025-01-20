def find_peaks_valleys(prices, n, m):
    peaks = []
    valleys = []
    
    i = 0
    while i < len(prices):
        if i + n <= len(prices) and all(prices[j] < prices[j+1] for j in range(i, i + n - 1)):
            if i + n < len(prices) and all(prices[j] > prices[j+1] for j in range(i + n, i + n + m - 1)):
                peaks.append(i)
            i += n
        elif i + m <= len(prices) and all(prices[j] > prices[j+1] for j in range(i, i + m - 1)):
            if i + m < len(prices) and all(prices[j] < prices[j+1] for j in range(i + m, i + m + n - 1)):
                valleys.append(i)
            i += m
        else:
            i += 1
    
    return len(peaks), len(valleys)

# Read input
import sys
input_data = sys.stdin.read().splitlines()
s, n, m = map(int, input_data[0].split())
prices = list(map(int, input_data[1:]))

# Find peaks and valleys
peaks, valleys = find_peaks_valleys(prices, n, m)

# Output result
print(peaks, valleys)