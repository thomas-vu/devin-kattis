def count_valid_times(h1, m1, h2, m2, alpha):
    def angle_between_hands(h, m):
        minute_angle = (m * 6) % 360
        hour_angle = (h * 30 + m * 0.5) % 360
        angle_diff = abs(hour_angle - minute_angle)
        if angle_diff > 180:
            angle_diff = 360 - angle_diff
        return angle_diff
    
    count = 0
    for hour in range(h1, h2 + 1):
        for minute in range(0, 60, int(180 / alpha)):
            if angle_between_hands(hour, minute) == alpha:
                count += 1
    return count

def main():
    t = int(input())
    results = []
    for _ in range(t):
        h1, m1, h2, m2, alpha = input().split()
        h1, m1, h2, m2 = int(h1), int(m1), int(h2), int(m2)
        alpha = int(alpha)
        results.append(count_valid_times(h1, m1, h2, m2, alpha))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()