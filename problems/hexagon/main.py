def min_score(positions, values):
    S = (len(positions) + 1) // 2
    min_score = float('inf')
    
    def is_end_configuration(config):
        if S == 5:
            return config in [(1, 5, 10, 15, 19), (3, 6, 10, 14, 17), (8, 9, 10, 11, 12)]
        elif S == 3:
            return config in [(1, 4, 7), (2, 5, 8)]
        elif S == 7:
            return config in [(1, 6, 11, 16, 21, 26, 31), (4, 7, 10, 13, 16, 19, 22), (8, 9, 10, 11, 12, 13, 14)]
        elif S == 9:
            return config in [(1, 8, 15, 22, 29, 36, 43, 50, 57), (6, 11, 16, 21, 26, 31, 36, 41, 46), (10, 12, 14, 16, 18, 20, 22, 24, 26)]
        else:
            return False
    
    def dfs(config, score):
        nonlocal min_score
        if is_end_configuration(config):
            min_score = min(min_score, score)
            return
        for i in range(len(config)):
            for dx, dy in [(-1, 0), (1, 0)]:
                nx, ny = config[i] + dx, (config[i] - 1) // S * 2 + dy
                if nx >= 0 and ny >= 0 and ny < S:
                    new_config = list(config)
                    new_config[i] = nx + ny * S
                    dfs(sorted(new_config), score + values[i])
    
    for i in range(len(positions)):
        dfs([positions[i] - 1], values[i])
    
    return min_score

def main():
    N = int(input())
    for case in range(1, N + 1):
        positions = list(map(int, input().split()))
        values = list(map(int, input().split()))
        result = min_score(positions, values)
        print(f"Case #{case}: {result}")

if __name__ == "__main__":
    main()