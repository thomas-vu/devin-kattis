import math

def calculate_radius(N, M):
    radius = 1 + (N - 1) * math.sqrt(2) * M
    return radius

def calculate_fence_length(N, M):
    fence = 2 * math.pi * (1 + (N - 1) * M)
    return fence

def main():
    P = int(input())
    for _ in range(P):
        K, N, M = map(int, input().split())
        radius_outermost = calculate_radius(N, M)
        fence_length = calculate_fence_length(N, M)
        print("{} {:.3f} {:.3f}".format(K, radius_outermost, fence_length))

if __name__ == "__main__":
    main()