def main():
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        
        jack_cds = set()
        for _ in range(N):
            jack_cds.add(int(input()))
        
        common_count = 0
        for _ in range(M):
            cd = int(input())
            if cd in jack_cds:
                common_count += 1
        
        print(common_count)

if __name__ == "__main__":
    main()