from itertools import product

def generate_codes(K):
    return [''.join(map(str, p)) for p in product('0123456789', repeat=K)]

def find_matching_codes(K, observations):
    codes = generate_codes(K)
    matching_codes = []
    
    for code in codes:
        if all(code in obs for obs in observations):
            matching_codes.append(code)
    
    return sorted(matching_codes)

def main():
    K, N = map(int, input().split())
    observations = [input() for _ in range(N)]
    
    matching_codes = find_matching_codes(K, observations)
    
    print(len(matching_codes))
    for code in matching_codes:
        print(code)

if __name__ == "__main__":
    main()