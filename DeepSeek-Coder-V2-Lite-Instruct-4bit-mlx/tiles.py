def count_ways(w, h):
    if w == 1 or h == 1:
        return w * h
    elif w == 2 or h == 2:
        if w == 2 and h == 2:
            return 1
        else:
            odd = (w * h + 1) // 2
            even = w * h - odd
            return odd if w == 2 else even
    else:
        return (w * h + 1) // 2

def main():
    n = int(input())
    for _ in range(n):
        a_lo, a_hi = map(int, input().split())
        max_ways = 0
        best_area = a_lo
        for a in range(a_lo, a_hi + 1):
            w = h = int(a**0.5)
            while w * h < a:
                w += 1
            while w * h > a:
                h -= 1
            ways = count_ways(w, h)
            if ways > max_ways:
                max_ways = ways
                best_area = a
        print(best_area, max_ways)

if __name__ == "__main__":
    main()