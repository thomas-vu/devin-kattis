def detect_silence(n, m, c, samples):
    silences = []
    for i in range(n - m + 1):
        subarray = samples[i:i + m]
        if max(subarray) - min(subarray) <= c:
            silences.append(i + 1)  # 1-indexed as per the problem statement
    return silences if silences else ['NONE']

# Read input
n, m, c = map(int, input().split())
samples = list(map(int, input().split()))

# Output the result
result = detect_silence(n, m, c, samples)
for line in result:
    print(line)