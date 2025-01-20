N = int(input())
if N == 0:
    print("++")
elif N == 1:
    print("+-+")
    print("| |")
    print("+-+")
else:
    square = ["+" + "-" * N + "+"]
    for i in range(N):
        square.append("|" + " " * N + "|")
    square.append("+" + "-" * N + "+")
    for line in square:
        print(line)