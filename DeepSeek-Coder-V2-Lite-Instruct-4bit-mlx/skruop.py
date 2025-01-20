volume = 7
n = int(input())
for _ in range(n):
    request = input()
    if request == "Skru op!":
        volume = min(volume + 1, 10)
    elif request == "Skru ned!":
        volume = max(volume - 1, 0)
print(volume)