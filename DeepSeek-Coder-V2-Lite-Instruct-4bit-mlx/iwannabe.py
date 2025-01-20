def read_ints():
    return list(map(int, input().split()))

N, K = read_ints()
pokenoms = [tuple(read_ints()) for _ in range(N)]

attack_indices = sorted(range(N), key=lambda i: pokenoms[i][0], reverse=True)
defense_indices = sorted(range(N), key=lambda i: pokenoms[i][1], reverse=True)
health_indices = sorted(range(N), key=lambda i: pokenoms[i][2], reverse=True)

attack_set = set(attack_indices[:K])
defense_set = set(defense_indices[:K])
health_set = set(health_indices[:K])

unique_pokenoms = attack_set.union(defense_set).union(health_set)
print(len(unique_pokenoms))