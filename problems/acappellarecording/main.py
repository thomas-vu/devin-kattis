def min_recordings(n, d, pitches):
    if n == 0:
        return 0
    recordings = 1
    min_pitch = max_pitch = pitches[0]
    
    for i in range(1, n):
        min_pitch = min(min_pitch, pitches[i])
        max_pitch = max(max_pitch, pitches[i])
        
        if (max_pitch - min_pitch) > d:
            recordings += 1
            min_pitch = max_pitch = pitches[i]
            
    return recordings

# Read input
n, d = map(int, input().split())
pitches = [int(input()) for _ in range(n)]

# Compute and output the result
print(min_recordings(n, d, pitches))