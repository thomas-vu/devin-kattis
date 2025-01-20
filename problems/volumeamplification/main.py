def closest_volume(n, y, amps):
    def find_closest(target):
        best = 1
        for mask in range(1 << len(amps)):
            product = 1
            for i, amp in enumerate(amps):
                if mask & (1 << i):
                    product *= amp
            best = max(best, min(product, target))
        return best
    
    closest_val = find_closest(y)
    return closest_val

def main():
    n = int(input())
    for _ in range(n):
        a, y = map(int, input().split())
        amps = list(map(int, input().split()))
        closest_val = closest_volume(a, y, amps)
        print(closest_val)

if __name__ == "__main__":
    main()