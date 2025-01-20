import sys

def spread_fire(forest, A, B):
    queue = [A]
    visited = set([A])
    
    while queue:
        current = queue.pop(0)
        x, y = divmod(current, 100)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 100 and 0 <= ny < 100 and (nx * 100 + ny) not in visited:
                neighbor = nx * 100 + ny
                if forest[neighbor] == 1:
                    queue.append(neighbor)
                    visited.add(neighbor)
                if neighbor == B:
                    return True
    return False

def main():
    while True:
        try:
            line = sys.stdin.readline().strip()
            if not line:
                break
            r, n = map(int, line.split())
            
            forest = [0] * 10000
            fires = []
            
            for i in range(n):
                while True:
                    m = (r * 5171 + 13297) % 50021
                    if forest[m] == 0:
                        forest[m] = 1
                        fires.append(m)
                        break
                    r = m
                
                if i < n - 1:
                    a = (r * fires[i % len(fires)]) % (i + 1)
                    b = (r * fires[i % len(fires)]) % (i + 1)
                    A = fires[a]
                    B = fires[b]
                    
                    if spread_fire(forest, A, B):
                        print(1, end=' ')
                    else:
                        print(0, end=' ')
                
                r = m
                
                if (i + 1) % 100 == 0:
                    print()
            
            sys.stdout.flush()
        except EOFError:
            break

if __name__ == "__main__":
    main()