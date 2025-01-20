def main():
    while True:
        try:
            n, s, m = map(int, input().split())
            board = list(map(int, input().split()))
            
            visited = [False] * n
            position = s - 1
            hops = 0
            
            while True:
                if position < 0 or position >= n:
                    fate = 'left' if position < 0 else 'right'
                    break
                elif board[position] == m:
                    fate = 'magic'
                    break
                elif visited[position]:
                    fate = 'cycle'
                    break
                
                visited[position] = True
                jump = board[position]
                position += jump
                hops += 1
            
            print(fate)
            print(hops)
        except EOFError:
            break

if __name__ == "__main__":
    main()