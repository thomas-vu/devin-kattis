def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    T = int(data[index + 1])
    index += 2
    
    A = int(data[index])
    B = int(data[index + 1])
    C = int(data[index + 2])
    t0 = int(data[index + 3])
    index += 4
    
    t = [0] * N
    t[0] = t0
    for i in range(1, N):
        t[i] = ((A * t[i - 1] + B) % C) + 1
    
    problems_solved = 0
    total_penalty = 0
    current_time = 0
    
    for i in range(N):
        if current_time + t[i] <= T:
            problems_solved += 1
            total_penalty = (total_penalty + current_time + t[i]) % 1000000007
            current_time += t[i]
        else:
            break
    
    print(problems_solved, total_penalty)

if __name__ == "__main__":
    main()