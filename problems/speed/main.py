def calculate_c(n, t, segments):
    total_distance = 0
    for distance, speed in segments:
        total_distance += distance
    
    left = min(min(speed for _, speed in segments), 0) - 1
    right = max(max(speed for _, speed in segments), 0) + 1
    
    while right - left > 1e-6:
        mid = (left + right) / 2
        time_taken = sum(distance / (speed + mid) for distance, speed in segments)
        if abs(time_taken - t) < 1e-6:
            return mid
        elif time_taken > t:
            left = mid
        else:
            right = mid
    return (left + right) / 2

def main():
    n, t = map(int, input().split())
    segments = [tuple(map(float, input().split())) for _ in range(n)]
    c = calculate_c(n, t, segments)
    print("{:.10f}".format(c))

if __name__ == "__main__":
    main()