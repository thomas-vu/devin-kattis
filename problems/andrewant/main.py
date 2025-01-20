def simulate_ants(L, A, ants):
    left_ants = []
    right_ants = []
    
    for pos, direction in ants:
        if direction == 'L':
            left_ants.append(pos)
        else:
            right_ants.append(pos)
    
    left_ants.sort()
    right_ants.sort()
    
    last_fall_time = 0
    if left_ants and right_ants:
        max_left = left_ants[-1]
        min_right = right_ants[0]
        if max_left > L - min_right:
            last_fall_time = (max_left + min_right) / 2
        else:
            last_fall_time = max(L - left_ants[0], right_ants[-1])
    elif left_ants:
        last_fall_time = L - left_ants[0]
    elif right_ants:
        last_fall_time = right_ants[-1]
    
    return int(last_fall_time)

def main():
    while True:
        try:
            L, A = map(int, input().split())
            ants = []
            for _ in range(A):
                pos, direction = input().split()
                ants.append((int(pos), direction))
            
            last_fall_time = simulate_ants(L, A, ants)
            if len(ants) == 2:
                print(f"The last ant will fall down in {last_fall_time} seconds - started at {ants[0][0]} and {ants[1][0]}.")
            else:
                print(f"The last ant will fall down in {last_fall_time} seconds - started at {ants[0][0]}.")
        except EOFError:
            break

if __name__ == "__main__":
    main()