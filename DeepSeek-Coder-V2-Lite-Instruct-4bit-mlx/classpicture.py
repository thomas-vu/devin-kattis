def find_order(n, names, m, dislikes):
    graph = {i: [] for i in range(n)}
    for u, v in dislikes:
        graph[u].append(v)
        graph[v].append(u)
    
    color = [-1] * n
    def dfs(node, c=0):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not dfs(i):
                return "You all need therapy."
    
    order = []
    for i in range(n):
        if color[i] == 0:
            order.append(names[i])
    for i in range(n):
        if color[i] == 1:
            order.append(names[i])
    
    return order

def main():
    while True:
        try:
            n = int(input())
            names = [input().strip() for _ in range(n)]
            m = int(input().strip())
            dislikes = [tuple(input().strip().split()) for _ in range(m)]
            dislikes = [(int(a) - 1, int(b) - 1) for a, b in dislikes]
            order = find_order(n, names, m, dislikes)
            print(' '.join(order))
        except EOFError:
            break

if __name__ == "__main__":
    main()