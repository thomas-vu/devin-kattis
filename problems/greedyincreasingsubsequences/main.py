def find_lis(seq):
    n = len(seq)
    lis = []
    for i in range(n):
        idx = len(lis)
        pos = bisect_left(lis, seq[i])
        if pos == len(lis):
            lis.append(seq[i])
        else:
            lis[pos] = seq[i]
    return len(lis)

def find_all_lis(seq):
    n = len(seq)
    lis_lengths = [0] * n
    prev = [-1] * n
    for i in range(n):
        lis_lengths[i] = 1 + max([lis_lengths[j] for j in range(i) if seq[j] < seq[i]], default=0)
        prev[i] = next((j for j in range(i) if seq[j] < seq[i]), -1)
    
    lis = []
    def build_lis(index):
        if index == -1:
            return []
        return build_lis(prev[index]) + [seq[index]]
    
    for i in range(n):
        if lis_lengths[i] == find_lis(seq):
            lis.append(build_lis(i))
    return lis

n = int(input())
seq = list(map(int, input().split()))
all_lis = find_all_lis(seq)
print(len(all_lis))
for lis in all_lis:
    print(' '.join(map(str, lis)))