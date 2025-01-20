from datetime import datetime, timedelta

def parse_time(start_time):
    return datetime.strptime(start_time, "%I:%M:%S %p")

def calculate_laps(start_time, records):
    start = parse_time(start_time)
    laps_dict = {}
    
    for record in records:
        time_str, name = record.split()
        lap_time = datetime.strptime(time_str, "%I:%M:%S %p")
        lap_seconds = (lap_time - start).total_seconds() / 60
        
        if lap_seconds >= 180:
            continue
        
        if name not in laps_dict:
            laps_dict[name] = {'laps': 0, 'last_lap_time': lap_seconds}
        
        laps_dict[name]['laps'] += 1
        laps_dict[name]['last_lap_time'] = lap_seconds
    
    return laps_dict

def main():
    start_time = input().strip()
    N = int(input().strip())
    records = [input().strip() for _ in range(N)]
    
    laps_dict = calculate_laps(start_time, records)
    
    participants = list(laps_dict.keys())
    participants.sort(key=lambda x: (-laps_dict[x]['laps'], laps_dict[x]['last_lap_time']))
    
    for participant in participants:
        print(f"{laps_dict[participant]['laps']} {participant}")

if __name__ == "__main__":
    main()