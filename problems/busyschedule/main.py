def convert_to_minutes(time_str):
    parts = time_str.split()
    hour, minute = map(int, parts[0].split(':'))
    period = parts[1]
    if period == 'a.m.' and hour == 12:
        hour = 0
    elif period == 'p.m.' and hour != 12:
        hour += 12
    return hour * 60 + minute

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        appointments = []
        for _ in range(n):
            time_str = input().strip()
            appointments.append(convert_to_minutes(time_str))
        
        appointments.sort()
        
        for time in appointments:
            hour = time // 60
            minute = time % 60
            if hour == 0:
                print(f"12:{minute:02d} a.m.")
            elif hour == 12:
                print(f"12:{minute:02d} p.m.")
            elif hour < 12:
                print(f"{hour}:{minute:02d} a.m.")
            else:
                print(f"{hour - 12}:{minute:02d} p.m.")
        
        print()

if __name__ == "__main__":
    main()