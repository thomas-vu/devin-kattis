import math

def time_to_infect(R, K, ships):
    min_time = float('inf')
    for ship in ships:
        x, y, rocket_speed, virus_spread_speed = ship
        distance = math.sqrt(x**2 + y**2)
        if distance <= R:
            time_to_reach = distance / rocket_speed
            max_spread_distance = (R - distance) * 2 + virus_spread_speed
            min_time = min(min_time, max_spread_distance / virus_spread_speed + time_to_reach)
    return min_time

def main():
    T = int(input())
    results = []
    for _ in range(T):
        R, K = map(int, input().split())
        ships = [list(map(int, input().split())) for _ in range(K)]
        result = time_to_infect(R, K, ships)
        results.append("{:.10f}".format(result))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()