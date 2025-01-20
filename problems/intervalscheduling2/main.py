def parse_time(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def extend_intervals(N, intervals):
    extended_intervals = []
    for i in range(N - 1):
        start, end = intervals[i]
        next_start, next_end = intervals[i + 1]
        if end < next_start:
            extended_intervals.append((start, end))
        else:
            new_end = min(end, next_start - (next_start - end) // 2)
            extended_intervals.append((start, new_end))
    extended_intervals.append(intervals[-1])
    return extended_intervals

N = int(input())
intervals = [tuple(map(parse_time, input().split(' - '))) for _ in range(N)]
extended_intervals = extend_intervals(N, intervals)
for start, end in extended_intervals:
    print(f"{start // 60:02d}:{start % 60:02d} - {end // 60:02d}:{end % 60:02d}")