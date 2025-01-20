from itertools import permutations

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def tsp_bruteforce(world, beepers):
    min_distance = float('inf')
    for path in permutations(beepers):
        current_distance = 0
        start = world['start']
        for beeper in path:
            current_distance += distance(start, beeper)
            start = beeper
        current_distance += distance(start, world['start'])
        min_distance = min(min_distance, current_distance)
    return min_distance

def main():
    scenarios = int(input())
    for _ in range(scenarios):
        x_size, y_size = map(int, input().split())
        start_x, start_y = map(int, input().split())
        num_beepers = int(input())
        beepers = []
        for _ in range(num_beepers):
            x, y = map(int, input().split())
            beepers.append((x, y))
        world = {
            'start': (start_x, start_y),
            'beepers': beepers
        }
        result = tsp_bruteforce(world, beepers)
        print(result)

if __name__ == "__main__":
    main()