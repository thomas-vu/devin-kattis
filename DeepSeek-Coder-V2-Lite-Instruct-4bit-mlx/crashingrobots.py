def process_commands(warehouse, robot):
    commands = {
        'L': lambda r: (r['direction'] - 1) % 4,
        'R': lambda r: (r['direction'] + 1) % 4,
        'F': lambda r: {0: (r['x'], r['y'] + 1),
                        1: (r['x'] + 1, r['y']),
                        2: (r['x'], r['y'] - 1),
                        3: (r['x'] - 1, r['y'])}.get(r['direction'], r)
    }
    
    for _ in range(robot['commands']['repeat']):
        robot['direction'] = commands[robot['commands']['action']](robot)['direction']
        next_pos = commands[robot['commands']['action']](robot)[next(iter(filter(lambda k: k != 'direction', robot))]['x']
        if next_pos[0] < 1:
            return f"Robot {robot['id']} crashes into the wall"
        elif next_pos[0] > warehouse['width']:
            return f"Robot {robot['id']} crashes into the wall"
        elif next_pos[1] < 1:
            return f"Robot {robot['id']} crashes into the wall"
        elif next_pos[1] > warehouse['height']:
            return f"Robot {robot['id']} crashes into the wall"
        for other_robot in warehouse['robots']:
            if robot['id'] != other_robot['id'] and next_pos == (other_robot['x'], other_robot['y']):
                return f"Robot {robot['id']} crashes into robot {other_robot['id']}"
    warehouse['robots'][warehouse['robots'].index(robot)] = robot
    return "OK"

def main():
    K = int(input())
    results = []
    for _ in range(K):
        A, B = map(int, input().split())
        N, M = map(int, input().split())
        robots = []
        for i in range(N):
            x, y, direction = input().split()
            robots.append({'id': i + 1, 'x': int(x), 'y': int(y), 'direction': {'N': 0, 'E': 1, 'S': 2, 'W': 3}[direction], 'commands': {}})
        for i in range(M):
            robot_id, action, repeat = input().split()
            robots[int(robot_id) - 1]['commands'] = {'action': action, 'repeat': int(repeat)}
        warehouse = {'width': A, 'height': B, 'robots': robots}
        result = []
        for robot in robots:
            res = process_commands(warehouse, robot)
            result.append(res)
        results.append("\n".join(result))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()