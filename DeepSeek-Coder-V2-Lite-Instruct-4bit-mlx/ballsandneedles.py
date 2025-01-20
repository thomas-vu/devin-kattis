def check_true_closed_chains(needles):
    from itertools import permutations
    
    def is_true_closed_chain(indexes):
        visited = set()
        for i in range(len(indexes)):
            if indexes[i] in visited:
                continue
            for j in range(i + 1, len(indexes)):
                if indexes[j] in visited:
                    continue
                needle1 = needles[indexes[i]]
                needle2 = needles[indexes[j]]
                if (needle1[0] == needle2[0] or needle1[0] == needle2[1] or needle1[1] == needle2[0] or needle1[1] == needle2[1]):
                    visited.add(indexes[i])
                    visited.add(indexes[j])
                    break
            else:
                return True
        return False
    
    n = len(needles)
    for i in range(n):
        for j in range(i + 1, n):
            if is_true_closed_chain([i, j] + list(range(n))):
                return True
    return False

def check_floor_closed_chains(needles):
    from itertools import permutations
    
    def is_floor_closed_chain(indexes):
        visited = set()
        for i in range(len(indexes)):
            if indexes[i] in visited:
                continue
            for j in range(i + 1, len(indexes)):
                if indexes[j] in visited:
                    continue
                needle1 = needles[indexes[i]]
                needle2 = needles[indexes[j]]
                shadow1 = (needle1[0], needle1[1]) if needle1[2] == needle1[5] else (needle1[3], needle1[4])
                shadow2 = (needle2[0], needle2[1]) if needle2[2] == needle2[5] else (needle2[3], needle2[4])
                if shadow1 == shadow2:
                    visited.add(indexes[i])
                    visited.add(indexes[j])
                    break
            else:
                return True
        return False
    
    n = len(needles)
    for i in range(n):
        for j in range(i + 1, n):
            if is_floor_closed_chain([i, j] + list(range(n))):
                return True
    return False

def main():
    K = int(input())
    needles = [tuple(map(int, input().split())) for _ in range(K)]
    
    true_closed = check_true_closed_chains(needles)
    floor_closed = check_floor_closed_chains(needles)
    
    print("True closed chains" if true_closed else "No true closed chains")
    print("Floor closed chains" if floor_closed else "No floor closed chains")

if __name__ == "__main__":
    main()