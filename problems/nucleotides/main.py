from collections import Counter

def most_prevalent_nucleotides(dna, s, e):
    section = dna[s-1:e]
    cnt = Counter(section)
    most_common = cnt.most_common()
    result = ''
    for _, nucleotide in most_common:
        result += nucleotide
    return result

dna = input().strip()
m = int(input().strip())
for _ in range(m):
    s, e = map(int, input().strip().split())
    result = most_prevalent_nucleotides(dna, s, e)
    print(result)