T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    a, b, d = map(int, input().split())
    
    # Calculate the total time for one trip including travel and mining time
    total_time = (b + d - a) % N
    
    # Check if the trip ends during day or night
    print("YES" if total_time < N - M else "NO")