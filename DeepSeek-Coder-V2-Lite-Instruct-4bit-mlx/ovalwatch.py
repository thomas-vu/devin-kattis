def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N, K = int(data[0]), int(data[1])
    legs = [tuple(map(int, data[i].split())) for i in range(2, K + 2)]
    
    assignments = [0] * N
    for i in range(N):
        current_line = i
        for leg in legs:
            if leg[0] == current_line:
                current_line = leg[1] + 1
            elif leg[0] == current_line - 1:
                current_line = leg[1] + 1
        assignments[i] = current_line - 1
    
    print(' '.join(map(str, assignments)))

main()