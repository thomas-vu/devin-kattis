def parse_cron_spec(spec):
    parts = spec.split()
    hours, minutes, seconds = parts[0], parts[1], parts[2]
    
    def parse_segment(segment):
        if segment == '*':
            return set(range(24) if 'h' in spec else range(60) if 'm' in spec else range(60))
        values = []
        for part in segment.split(','):
            if '-' in part:
                start, end = map(int, part.split('-'))
                values.extend(range(start, end + 1))
            else:
                values.append(int(part))
        return set(values)
    
    hours_set = parse_segment(hours)
    minutes_set = parse_segment(minutes)
    seconds_set = parse_segment(seconds)
    
    return hours_set, minutes_set, seconds_set

def count_job_starts(specs):
    total_seconds = 0
    job_start_count = 0
    time_map = [[[0 for _ in range(60)] for _ in range(60)]
    
    for spec in specs:
        hours_set, minutes_set, seconds_set = parse_cron_spec(spec)
        for hour in hours_set:
            for minute in minutes_set:
                for second in seconds_set:
                    if time_map[hour][minute][second] == 0:
                        time_map[hour][minute][second] = 1
                        total_seconds += 1
                        job_start_count += 1
    
    return total_seconds, job_start_count

n = int(input())
specs = [input().strip() for _ in range(n)]
total_seconds, job_start_count = count_job_starts(specs)
print(total_seconds, job_start_count)