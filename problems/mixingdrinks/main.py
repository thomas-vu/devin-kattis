MOD = 10**9 + 7

def main():
    N, P = map(int, input().split())
    bad_pairs = set()
    for _ in range(P):
        a, b = map(int, input().split())
        bad_pairs.add((min(a, b), max(a, b)))
    
    def can_form_drink(used, bad_pairs):
        for pair in bad_pairs:
            if pair[0] < used[-1] < pair[1]:
                return False
        return True
    
    def count_ways(N, bad_pairs):
        drinks = [0] * (N + 1)
        drinks[0] = 1
        for i in range(1, N + 1):
            ways = 0
            for j in range(i):
                if (j + 1, i) not in bad_pairs and can_form_drink([j + 1], bad_pairs):
                    ways = (ways + drinks[j]) % MOD
            drinks[i] = ways
        return drinks[N]
    
    result = count_ways(N, bad_pairs)
    print(result)

if __name__ == "__main__":
    main()