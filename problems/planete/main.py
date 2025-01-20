def calculate_event_durations(N, M, observations):
    event_durations = [0] * M
    min_duration = 1
    max_duration = 365
    
    for obs in observations:
        start_day, start_month = int(obs[0]), int(obs[1])
        end_day, end_month = int(obs[2]), int(obs[3])
        event_counts = obs[4:]
        
        for i in range(M):
            if event_counts[i] > 0:
                duration = int(obs[2]) - int(obs[0]) + 1
                if min_duration <= duration <= max_duration:
                    event_durations[i] += 1
    
    return event_durations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N, M = int(data[0]), int(data[1])
    observations = [data[i:i + M + 4] for i in range(2, N * (M + 4) + 2, M + 4)]
    
    result = calculate_event_durations(N, M, observations)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()