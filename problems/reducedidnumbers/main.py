def find_smallest_modulus(sins):
    sin_set = set()
    for sin in sins:
        if sin not in sin_set:
            sin_set.add(sin)
        else:
            return True  # This should never happen due to the problem statement
    max_sin = max(sins)
    for m in range(1, max_sin + 1):
        if len(set([sin % m for sin in sins])) == len(sins):
            return m
    return max_sin + 1

def main():
    G = int(input())
    sins = [int(input()) for _ in range(G)]
    print(find_smallest_modulus(sins))

if __name__ == "__main__":
    main()