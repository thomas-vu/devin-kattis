import sys

def cover_intervals(A, B, intervals):
    covered = A
    count = 0
    indices = []
    while covered < B:
        max_end = -1
        best_interval = None
        for i, (a, b) in enumerate(intervals):
            if a <= covered and b > max_end:
                max_end = b
                best_interval = (a, b, i)
        if best_interval is None:
            return "impossible"
        covered = max_end
        indices.append(best_interval[2])
        count += 1
    return count, indices

def main():
    while True:
        try:
            A, B = map(float, sys.stdin.readline().strip().split())
        except EOFError:
            break
        n = int(sys.stdin.readline().strip())
        intervals = []
        for i in range(n):
            a, b = map(float, sys.stdin.readline().strip().split())
            intervals.append((a, b, i))
        result = cover_intervals(A, B, intervals)
        if result == "impossible":
            print("impossible")
        else:
            count, indices = result
            print(count)
            if count > 0:
                print(" ".join(map(str, indices)))

if __name__ == "__main__":
    main()