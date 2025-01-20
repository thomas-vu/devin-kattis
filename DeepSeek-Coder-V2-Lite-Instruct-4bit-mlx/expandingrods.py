import math

def compute_displacement(L, n, C):
    L_new = (1 + n * C) * L
    theta = math.asin((L_new - L) / L)
    return (L / 2) * math.tan(theta / 2)

def main():
    while True:
        L, n, C = map(float, input().split())
        if L == -1 and n == -1 and C == -1:
            break
        displacement = compute_displacement(L, n, C)
        print("{:.9f}".format(displacement))

if __name__ == "__main__":
    main()