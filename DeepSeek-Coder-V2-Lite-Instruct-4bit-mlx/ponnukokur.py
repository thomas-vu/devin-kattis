n, q = map(int, input().split())
flips = [0] * n
flip_all = 0

for _ in range(q):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        i = operation[1] - 1
        flips[i] ^= 1
    elif operation[0] == 2:
        flip_all ^= 1
    else:
        l, r = operation[1] - 1, operation[2] - 1
        count_ones = sum(flips[l:r+1]) if flip_all == 0 else (r - l + 1) - sum(flips[l:r+1])
        print(count_ones)