def main():
    N = int(input())
    visibility = [list(map(int, input().split('-'))) for _ in range(N)]
    
    # Create adjacency list to represent the visibility relations
    adj_list = [[] for _ in range(N + 1)]
    for u, v in visibility:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Assign species to enclosures using a backtracking approach
    def assign_species(enclosure):
        if enclosure > N:
            for i in range(1, N + 1):
                print(i, end=' ')
                if species[i] == 0:
                    continue
                elif species[i] == 1:
                    print('Lion', end=' ')
                elif species[i] == 2:
                    print('Leopard', end=' ')
                elif species[i] == 3:
                    print('Tiger', end=' ')
                else:
                    print('Panther', end=' ')
            exit()
        
        for specie in range(1, 5):
            if is_safe(enclosure, specie):
                species[enclosure] = specie
                assign_species(enclosure + 1)
                species[enclosure] = 0
    
    def is_safe(enclosure, specie):
        for neighbor in adj_list[enclosure]:
            if species[neighbor] == specie:
                return False
        return True
    
    # Initialize the species array with 0 (no assigned species)
    species = [0] * (N + 1)
    
    # Start the backtracking algorithm from enclosure 1
    assign_species(1)

if __name__ == "__main__":
    main()