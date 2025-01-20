def can_move(map_, r1, c1, r2, c2):
    start = map_[r1 - 1][c1 - 1]
    end = map_[r2 - 1][c2 - 1]
    
    if start == end:
        return 'binary' if start == '0' else 'decimal'
    else:
        return 'neither'

def main():
    r, c = map(int, input().split())
    map_ = [input() for _ in range(r)]
    
    n = int(input())
    for _ in range(n):
        r1, c1, r2, c2 = map(int, input().split())
        result = can_move(map_, r1, c1, r2, c2)
        print(result)

if __name__ == "__main__":
    main()