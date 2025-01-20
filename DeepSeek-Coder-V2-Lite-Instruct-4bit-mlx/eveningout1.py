A, B = map(int, input().split())
coins_needed = (B - A % B) % B
print(coins_needed if coins_needed <= B / 2 else B - coins_needed)