N = int(input())
for _ in range(N):
    line = input().strip()
    if line.startswith("Simon says"):
        print(line[len("Simon says") + 1:])