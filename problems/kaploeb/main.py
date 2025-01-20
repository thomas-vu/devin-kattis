def main():
    l, k, s = map(int, input().split())
    participants = {}
    
    for _ in range(l):
        start_number, lap_time = input().split()
        minutes, seconds = map(float, lap_time.split('.'))
        total_time = minutes * 60 + seconds
        participants[int(start_number)] = total_time
    
    completed_participants = sorted([(start_number, time) for start_number, time in participants.items() if sum([1 for t in participants.values() if t <= time]) >= k], key=lambda x: (x[1], x[0]))
    
    for participant in completed_participants:
        print(participant[0])

if __name__ == "__main__":
    main()