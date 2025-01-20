def solve():
    n = int(input())
    candies = list(map(int, input().split()))
    
    total_candies = sum(candies)
    
    if total_candies % n == 0:
        print(n)
        print(' '.join(map(str, range(1, n + 1))))
    else:
        print(-1)

solve()