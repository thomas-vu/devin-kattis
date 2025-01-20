N = int(input())
lengths = [int(input()) for _ in range(N)]
total_length = sum(lengths) - (N - 1)
print(total_length)