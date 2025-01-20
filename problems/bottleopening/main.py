def open_bottles(n, k):
    if k > n or (k == 1 and n == 2) or (k % 2 != 0 and k > 3):
        print("impossible")
    else:
        for i in range(1, k + 1):
            print("open", i, "using", n)

# Read input
n = int(input())
k = int(input())

open_bottles(n, k)