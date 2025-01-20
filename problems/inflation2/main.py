N = int(input())
prices = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    event = input().split()
    if event[0] == 'INFLATION':
        x = int(event[1])
        for i in range(N):
            prices[i] += x
    elif event[0] == 'SET':
        x = int(event[1])
        y = int(event[2])
        for i in range(N):
            if prices[i] == x:
                prices[i] = y
    print(sum(prices))