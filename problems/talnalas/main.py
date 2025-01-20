import sys
from collections import deque

def rotate(digit, direction):
    if direction == 'left':
        return (digit - 1) % 10
    else:
        return (digit + 1) % 10

def is_lucky(number, lucky_numbers):
    return number in lucky_numbers

def bfs(initial, goal, lucky_numbers):
    n = len(initial)
    queue = deque([(initial, 0, [])])
    visited = set()
    
    while queue:
        current, steps, path = queue.popleft()
        if current == goal:
            return path, steps
        for i in range(n):
            left_digit = rotate(current[i], 'left')
            right_digit = rotate(current[i], 'right')
            for next_digit in [left_digit, right_digit]:
                if is_lucky(next_digit, lucky_numbers):
                    next_state = list(current)
                    next_state[i] = next_digit
                    next_state = tuple(next_state)
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, steps + 1, path + [next_digit]))
    return None, sys.maxsize

def main():
    n, m = map(int, input().split())
    initial = tuple(map(int, list(input())))
    goal = tuple(map(int, list(input())))
    lucky_numbers = set([tuple(map(int, list(input()))) for _ in range(m)])
    
    path, steps = bfs(initial, goal, lucky_numbers)
    
    if steps == sys.maxsize:
        print("Neibb")
    else:
        print(steps)
        for state in path:
            print(''.join(map(str, state)))

if __name__ == "__main__":
    main()