def main():
    N = int(input())
    photos = [list(map(int, pair.split())) for _ in range(5) for pair in input().split('\n')[-1].split('  ')[1:]]
    
    parties = [0] * N
    for photo in photos:
        K, pairs = photo[0], photo[1:]
        for i in range(K):
            for j in range(i+1, K):
                a, b = pairs[i] - 1, pairs[j] - 1
                if parties[a] == 0 and parties[b] == 0:
                    parties[a], parties[b] = 'A', 'B'
                elif parties[a] == 0:
                    parties[a] = 'A' if parties[b] != 'B' else 'B'
                elif parties[b] == 0:
                    parties[b] = 'B' if parties[a] != 'A' else 'A'
                elif parties[a] == parties[b]:
                    print("Invalid Input")
                    return
    
    result = ''.join(parties)
    print(result)

if __name__ == "__main__":
    main()