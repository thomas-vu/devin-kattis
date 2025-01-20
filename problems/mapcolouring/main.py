def can_color_with_four(graph, countries):
    for color in range(1, 5):
        if is_colorable(graph, countries, color):
            return True
    return False

def is_colorable(graph, countries, color):
    colors = [-1] * countries
    for i in range(countries):
        if colors[i] == -1:
            if not color_node(graph, i, color, colors):
                return False
    return True

def color_node(graph, node, color, colors):
    if colors[node] != -1:
        return colors[node] == color
    colors[node] = color
    for neighbor in graph[node]:
        if not color_node(graph, neighbor, 1 if color == 2 else 2, colors):
            return False
    return True

def main():
    T = int(input())
    for _ in range(T):
        C, B = map(int, input().split())
        graph = {i: [] for i in range(C)}
        for _ in range(B):
            i, j = map(int, input().split())
            graph[i].append(j)
            graph[j].append(i)
        if can_color_with_four(graph, C):
            print('many')
        else:
            print(4)

if __name__ == "__main__":
    main()