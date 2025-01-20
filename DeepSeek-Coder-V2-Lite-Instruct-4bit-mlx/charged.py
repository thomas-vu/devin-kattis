def main():
    n, m, q = map(int, input().split())
    grid = [['.' for _ in range(m)] for _ in range(n)]
    particles = {}
    
    for _ in range(q):
        x, y, s = input().split()
        particles[(int(x) - 1, int(y) - 1)] = s
    
    for y in range(n):
        for x in range(m):
            potential = 0
            for (px, py), charge in particles.items():
                distance = ((x - px)**2 + (y - py)**2)**0.5
                if distance == 0:
                    potential = float('inf') if charge == '+' else -float('inf')
                    break
                potential += int(charge) / distance
            if potential == float('inf'):
                grid[y][x] = '+'
            elif potential == -float('inf'):
                grid[y][x] = '-'
            else:
                potential_str = f"{potential:.2f}".rstrip('0').rstrip('.')
                if potential > 1 / (3.14**2):
                    grid[y][x] = '0' if potential > 0 else '%'
                elif potential > 1 / (3.14**3):
                    grid[y][x] = 'O' if potential > 0 else 'o'
                elif potential < -1 / (3.14**2):
                    grid[y][x] = 'X' if potential < 0 else 'x'
                elif potential < -1 / (3.14**3):
                    grid[y][x] = 'o' if potential < 0 else 'O'
                elif potential < -1 / (3.14):
                    grid[y][x] = 'x' if potential < 0 else 'X'
    
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()