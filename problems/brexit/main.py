def will_leave(C, P, X, L, partnerships):
    # Create adjacency list for the graph
    adj_list = {i: [] for i in range(1, C+1)}
    for A_i, B_i in partnerships:
        adj_list[A_i].append(B_i)
        adj_list[B_i].append(A_i)
    
    # Initialize the number of partners each country will leave for
    leaves = {i: 0 for i in range(1, C+1)}
    
    # Start with the initially leaving country
    leaves[L] = 1
    
    # Use BFS to determine the number of partners each country will leave for
    queue = [L]
    while queue:
        current = queue.pop(0)
        for partner in adj_list[current]:
            if leaves[partner] == 0:
                # Calculate the number of partners that will leave for this partner
                leaving_partners = 0
                for p in adj_list[partner]:
                    if leaves[p] == 1:
                        leaving_partners += 1
                # If at least half of the partners leave, this partner will also leave
                if leaving_partners * 2 >= len(adj_list[partner]):
                    leaves[partner] = 1
                    queue.append(partner)
    
    # Determine if the home country will stay or leave
    return "leave" if leaves[X] == 1 else "stay"

# Read input
C, P, X, L = map(int, input().split())
partnerships = [tuple(map(int, input().split())) for _ in range(P)]

# Output the result
print(will_leave(C, P, X, L, partnerships))