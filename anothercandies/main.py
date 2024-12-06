T = int(input())

for _ in range(T):
    input()  # blank line
    N = int(input())
    total = 0
    
    for _ in range(N):
        total = (total + int(input())) % N
        
    print("YES" if total == 0 else "NO")
