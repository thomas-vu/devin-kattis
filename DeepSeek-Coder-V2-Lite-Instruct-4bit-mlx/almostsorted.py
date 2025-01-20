import sys
input = sys.stdin.read
lines = input().split()
n = int(lines[0])
arr = list(map(int, lines[1].split()))
Q = int(lines[2])

def cycle_sort(arr, Q):
    i = 0
    while i < n:
        if arr[i] == Q and all(arr[j] <= Q for j in range(i)):
            break
        while arr[i] != Q:
            val = arr[i]
            j = i
            while True:
                k = (val - 1) // 2
                if arr[k] == Q:
                    break
                arr[i], arr[k] = arr[k], arr[i]
            i += 1
    return arr

sorted_arr = cycle_sort(arr, Q)
print(" ".join(map(str, sorted_arr)))