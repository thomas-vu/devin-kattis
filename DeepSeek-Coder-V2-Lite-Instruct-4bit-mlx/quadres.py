def legendre_symbol(a, p):
    if a % p == 0:
        return 0
    else:
        return pow(a, (p - 1) // 2, p)

def solve_quadratic_residue(a, p):
    if legendre_symbol(a, p) == 1:
        return "yes"
    else:
        return "no"

def main():
    n = int(input())
    for _ in range(n):
        a, p = map(int, input().split())
        print(solve_quadratic_residue(a, p))

if __name__ == "__main__":
    main()