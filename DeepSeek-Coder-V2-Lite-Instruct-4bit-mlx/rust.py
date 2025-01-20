def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    map_data = data[2:]
    
    max_val = 0
    
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            total_val = 0
            for x in range(i, i + K):
                for y in range(j, j + K):
                    if map_data[x][y] == '#':
                        break
                    elif map_data[x][y] != '.':
                        total_val += int(map_data[x][y])
                else:
                    continue
                break
            else:
                max_val = max(max_val, total_val)
    
    print(max_val)

if __name__ == "__main__":
    main()