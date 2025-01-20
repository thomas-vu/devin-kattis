def calculate_happiness(a, b, c, t):
    # Calculate the maximum happiness for a given temperature
    return a * t**2 + b * t + c

def find_optimal_temperature(finns):
    # Binary search to find the optimal temperature for maximizing happiness
    left, right = 0, 100000
    while right - left > 1e-5:
        mid = (left + right) / 2
        happiness_mid = sum(calculate_happiness(a, b, c, mid) for a, b, c, _ in finns if mid <= t)
        happiness_mid_plus = sum(calculate_happiness(a, b, c, mid + 1) for a, b, c, t in finns if mid + 1 <= t)
        
        if happiness_mid < happiness_mid_plus:
            left = mid
        else:
            right = mid
    return (left + right) / 2

def main():
    N = int(input())
    finns = [tuple(map(int, input().split())) for _ in range(N)]
    optimal_temp = find_optimal_temperature(finns)
    max_happiness = sum(calculate_happiness(a, b, c, optimal_temp) for a, b, c, t in finns if optimal_temp <= t)
    print("{:.10f}".format(max_happiness))

if __name__ == "__main__":
    main()