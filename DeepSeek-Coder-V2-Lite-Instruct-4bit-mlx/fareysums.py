from fractions import Fraction

def farey_sum(N):
    sequence = []
    for b in range(1, N + 1):
        for a in range(b + 1):
            if Fraction(a, b).numerator == a and Fraction(a, b).denominator == b:
                sequence.append((a, b))
    sequence = sorted(sequence, key=lambda x: (x[1], x[0]))
    
    sum_fractions = 0
    for i in range(len(sequence) - 1):
        a1, b1 = sequence[i]
        a2, b2 = sequence[i + 1]
        sum_fractions += Fraction(a1, b1) / Fraction(a2, b2)
    
    return sum_fractions.limit_denominator()

def main():
    P = int(input())
    for _ in range(P):
        K, N = map(int, input().split())
        result = farey_sum(N)
        if result.denominator == 1:
            print(f"{K} {result.numerator}")
        else:
            print(f"{K} {result}")

if __name__ == "__main__":
    main()