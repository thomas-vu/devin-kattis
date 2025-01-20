def is_palindrome(s):
    return s == s[::-1]

def next_nucleotide(nuc):
    nucleotides = ['A', 'G', 'T', 'C']
    return nucleotides[(nucleotides.index(nuc) + 1) % 4]

def prev_nucleotide(nuc):
    nucleotides = ['A', 'G', 'T', 'C']
    return nucleotides[(nucleotides.index(nuc) - 1) % 4]

def solve_case(sequence, subsets):
    n = len(sequence)
    
    for subset in subsets:
        subseq = [sequence[i] for i in subset]
        if not is_palindrome(subseq):
            return "NO"
    
    # Check if we can transform the sequence to form palindromes for each subset
    for i in range(n):
        if not is_palindrome([sequence[j] for j in range(i, n) if (j - i) % 2 == 0]):
            return "NO"
    
    for i in range(n):
        if not is_palindrome([sequence[j] for j in range(i, n) if (j - i) % 2 == 1]):
            return "NO"
    
    for i in range(n):
        if not is_palindrome([sequence[j] for j in range(i, n) if (j - i) % 2 == 0]):
            return "NO"
    
    for i in range(n):
        if not is_palindrome([sequence[j] for j in range(i, n) if (j - i) % 2 == 1]):
            return "NO"
    
    return "YES"

def main():
    while True:
        N, T = map(int, input().split())
        if N == 0 and T == 0:
            break
        sequence = input().strip()
        subsets = []
        for _ in range(T):
            parts = input().split(':')
            L = int(parts[0])
            indices = list(map(int, parts[1].split()))
            subsets.append(indices)
        print(solve_case(sequence, subsets))

if __name__ == "__main__":
    main()