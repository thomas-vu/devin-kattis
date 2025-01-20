def main():
    n, s = map(int, input().split())
    refills = 0
    
    for _ in range(n):
        order = input().strip()
        x = int(order[:-1]) if 'L' not in order else int(order[:-1]) + 1
        s -= x
        if s < 0:
            refills += 1
            s = int(order[:-1]) if 'L' not in order else int(order[:-1]) + 9
    
    print(refills)

main()