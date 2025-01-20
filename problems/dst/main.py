def calculate_new_time(direction, minutes_change, hours, mins):
    total_minutes = (hours * 60 + mins + minutes_change) % 1440
    new_hours = total_minutes // 60
    new_mins = total_minutes % 60
    return f"{new_hours} {new_mins}"

def main():
    n = int(input())
    for _ in range(n):
        direction, D, H, M = input().split()
        D = int(D)
        H = int(H)
        M = int(M)
        
        if direction == 'F':
            new_time = calculate_new_time('F', D, H, M)
        else:
            new_time = calculate_new_time('B', D, H, M)
        
        print(new_time)

if __name__ == "__main__":
    main()