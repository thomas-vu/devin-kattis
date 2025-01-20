T = int(input())
for _ in range(T):
    command = input().strip()
    if command.lower().startswith("simon says"):
        print(command[len("simon says") + 1:].strip())
    else:
        print()