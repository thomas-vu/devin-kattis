def calculate_escape_count(robots, holes, threshold):
    escape_count = 0
    for robot in robots:
        min_distance = float('inf')
        for hole in holes:
            distance = ((robot[0] - hole[0]) ** 2 + (robot[1] - hole[1]) ** 2) ** 0.5
            if distance < min_distance:
                min_distance = distance
        if min_distance / 10 <= threshold:
            escape_count += 1
    return escape_count

def main():
    scenario_number = 0
    while True:
        m = int(input())
        if m == 0:
            break
        scenario_number += 1
        robots = [tuple(map(float, input().split())) for _ in range(m)]
        n = int(input())
        holes = [tuple(map(float, input().split())) for _ in range(n)]
        
        escape_5 = calculate_escape_count(robots, holes, 5)
        escape_10 = calculate_escape_count(robots, holes, 10)
        escape_20 = calculate_escape_count(robots, holes, 20)
        
        print(f"Scenario {scenario_number}")
        print(f"In 5 seconds {escape_5} robot(s) can escape")
        print(f"In 10 seconds {escape_10} robot(s) can escape")
        print(f"In 20 seconds {escape_20} robot(s) can escape")
        print()

if __name__ == "__main__":
    main()