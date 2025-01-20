def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def distance(a, b, c, d):
    return abs(a - c) + abs(b - d)

def min_cabs_required(rides):
    max_end_time = -1
    for ride in rides:
        _, start_h, start_m, end_h, end_m = ride
        start_time = time_to_minutes(f"{start_h:02d}:{start_m:02d}")
        end_time = time_to_minutes(f"{end_h:02d}:{end_m:02d}")
        max_end_time = max(max_end_time, end_time)
    
    required_cabs = 0
    current_time = -1
    for ride in rides:
        start_h, start_m, end_h, end_m = ride[1:]
        start_time = time_to_minutes(f"{start_h:02d}:{start_m:02d}")
        end_time = time_to_minutes(f"{end_h:02d}:{end_m:02d}")
        if current_time == -1 or current_time + distance(start_h, start_m, end_h, end_m) < start_time - 1:
            required_cabs += 1
            current_time = end_time
    return required_cabs

def main():
    N = int(input())
    for _ in range(N):
        M = int(input())
        rides = [tuple(map(int, input().split())) for _ in range(M)]
        rides = [(time_to_minutes(f"{h:02d}:{m:02d}"), a, b, c, d) for h, m, a, b, c, d in rides]
        rides.sort()
        print(min_cabs_required(rides))

if __name__ == "__main__":
    main()