def find_exit(room, W, L):
    for i in range(L):
        for j in range(W):
            if room[i][j] == '*':
                entry_x, entry_y = i, j
            elif room[i][j] == '&':
                exit_x, exit_y = i, j
            elif room[i][j] == '/':
                if (entry_x + entry_y) % 2 == 0:
                    exit_x, exit_y = i - min(entry_x, entry_y), j + min(entry_x, entry_y)
                else:
                    exit_x, exit_y = i + min(entry_x, W - entry_y - 1), j - min(entry_x, W - entry_y - 1)
            elif room[i][j] == '\\':
                if (entry_x + entry_y) % 2 == 0:
                    exit_x, exit_y = i + min(entry_x, entry_y), j - min(entry_x, entry_y)
                else:
                    exit_x, exit_y = i - min(entry_x, W - entry_y - 1), j + min(entry_x, W - entry_y - 1)
    room[exit_x][exit_y] = '&'
    return room

def main():
    T = int(input())
    for t in range(1, T + 1):
        W, L = map(int, input().split())
        room = [list(input().strip()) for _ in range(L)]
        room = find_exit(room, W, L)
        print("HOUSE", t)
        for line in room:
            print(''.join(line))
        if t < T:
            input()  # consume the empty line after each test case except the last one

if __name__ == "__main__":
    main()