def can_play_all_frequencies(f, frequency_data):
    for freq in frequency_data:
        ti, ni = freq
        intervals = [list(map(int, input().split())) for _ in range(ni)]
        total_time = 0
        pause_time = 0
        
        for i in range(ni):
            start, end = intervals[i]
            if i > 0:
                pause_time += (intervals[i][0] - intervals[i-1][1])
            total_time += (end - start) + pause_time
        
        if total_time != ti:
            return "impossible"
    return "possible"

f = int(input())
frequency_data = [tuple(map(int, input().split())) for _ in range(f)]
print(can_play_all_frequencies(f, frequency_data))