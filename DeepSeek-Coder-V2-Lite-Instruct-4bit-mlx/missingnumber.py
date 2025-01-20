n = int(input())
digits = input()

for i in range(1, n + 1):
    if str(i) not in digits:
        print(i)
        break