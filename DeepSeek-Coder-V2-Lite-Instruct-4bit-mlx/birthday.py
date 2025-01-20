def can_invite_all(p, connections):
    # Create adjacency list for the graph
    adj_list = [[] for _ in range(p)]
    for a, b in connections:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    # Check for bipartite graph using BFS
    color = [-1] * p  # -1: uncolored, 0: color A, 1: color B
    for i in range(p):
        if color[i] == -1:  # If not colored, start BFS from this node
            color[i] = 0
            queue = [i]
            while queue:
                node = queue.pop(0)
                for neighbor in adj_list[node]:
                    if color[neighbor] == -1:  # If neighbor is uncolored, color it with opposite color
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:  # If neighbor has the same color, not bipartite
                        return "Yes"
    return "No"

# Main function to process input and output results
def main():
    while True:
        p, c = map(int, input().split())
        if p == 0 and c == 0:
            break
        connections = [tuple(map(int, input().split())) for _ in range(c)]
        result = can_invite_all(p, connections)
        print(result)

if __name__ == "__main__":
    main()