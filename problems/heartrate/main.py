def calculate_abpm(b, p):
    t = p / (b - 1) if b > 2 else float('inf')
    min_abpm = 60 / t if b > 2 else float('inf')
    max_abpm = 60 / (t / b) if b > 2 else float('inf')
    calculated_bpm = 60 * b / p
    return min_abpm, calculated_bpm, max_abpm

def main():
    N = int(input())
    results = []
    for _ in range(N):
        b, p = map(float, input().split())
        min_abpm, calculated_bpm, max_abpm = calculate_abpm(int(b), p)
        results.append((min_abpm, calculated_bpm, max_abpm))
    
    for min_abpm, calculated_bpm, max_abpm in results:
        print("{:.4f} {:.4f} {:.4f}".format(min_abpm, calculated_bpm, max_abpm))

if __name__ == "__main__":
    main()