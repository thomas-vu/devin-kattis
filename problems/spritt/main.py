n, x = map(int, input().split())
needed = [int(input()) for _ in range(n)]
total_needed = sum(needed)
if total_needed <= x:
    print("Jebb")
else:
    print("Neibb")