def calculate_blood(child, relations):
    blood = 0.0
    while child in relations:
        parent1, parent2 = relations[child]
        blood += 0.5 ** (len(relations[child]))
        child = parent1
    return blood

def main():
    N, M = map(int, input().split())
    founder = input()
    relations = {}
    
    for _ in range(N):
        child, parent1, parent2 = input().split()
        relations[child] = (parent1, parent2)
    
    claimants = {}
    for _ in range(M):
        claimant = input()
        claimants[claimant] = calculate_blood(claimant, relations)
    
    most_related = max(claimants.items(), key=lambda x: x[1])
    print(most_related[0])

if __name__ == "__main__":
    main()