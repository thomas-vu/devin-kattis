def find_cia_blimps(codes):
    cia_indices = []
    for index, code in enumerate(codes):
        if 'CIA' in code:
            cia_indices.append(index + 1)
    return cia_indices if cia_indices else ["HE GOT AWAY!"]

codes = [input() for _ in range(5)]
result = find_cia_blimps(codes)
print(*result)