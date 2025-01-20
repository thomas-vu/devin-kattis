def main():
    n, m = map(int, input().split())
    switches = [input().split() for _ in range(m)]
    
    states = ['L'] * m
    
    for _ in range(n):
        for i, (state, left, right) in enumerate(switches):
            if state == 'L' and states[i] == 'L':
                states[left] = 'R' if states[left] == 'L' else 'L'
            elif state == 'R' and states[i] == 'R':
                states[right] = 'L' if states[right] == 'R' else 'R'
    
    print(''.join(states))

if __name__ == "__main__":
    main()