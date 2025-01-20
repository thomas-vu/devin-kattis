MOD = 10**9 + 7

def main():
    N, T = map(int, input().split())
    A, B, C, t0 = map(int, input().split())
    
    problems_solved = 0
    total_penalty = 0
    current_time = t0
    
    for _ in range(N):
        if current_time <= T:
            problems_solved += 1
            total_penalty = (total_penalty + current_time) % MOD
            current_time += ((A * t0 + B) % C) + 1
        else:
            break
    
    print(problems_solved, total_penalty)

if __name__ == "__main__":
    main()