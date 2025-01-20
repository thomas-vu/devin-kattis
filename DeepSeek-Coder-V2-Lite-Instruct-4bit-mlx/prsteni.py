from fractions import Fraction
import sys

def main():
    N = int(sys.stdin.readline().strip())
    radii = list(map(int, sys.stdin.readline().strip().split()))
    
    first_ring = radii[0]
    for i in range(1, N):
        ratio = Fraction(first_ring, radii[i])
        print(f"{ratio.numerator}/{ratio.denominator}")

if __name__ == "__main__":
    main()