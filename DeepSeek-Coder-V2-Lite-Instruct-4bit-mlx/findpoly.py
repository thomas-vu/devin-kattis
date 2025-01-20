from collections import defaultdict, deque
import sys

def parse_input(lines):
    segments = []
    for line in lines:
        parts = line.split()
        for part in parts:
            if ';' in part:
                points = part.split(';')
                for pt in points:
                    x1, y1, x2, y2 = map(int, pt.split(',')[:4])
                    segments.append(((x1, y1), (x2, y2)))
    return segments

def build_graph(segments):
    graph = defaultdict(list)
    for (a, b), (c, d) in segments:
        if a == c or a == d or b == c or b == d:
            graph[a].append(b)
            graph[b].append(a)
    return graph

def is_polygon(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
    return len(visited) == len(graph)

def count_figures_and_polygons(segments):
    graph = build_graph(segments)
    figures = set()
    while segments:
        start = segments[0][0]
        queue = deque([start])
        figure_segments = set()
        while queue:
            node = queue.popleft()
            if node not in figure_segments:
                figure_segments.add(node)
                for segment in segments[:]:
                    if node == segment[0] or node == segment[1]:
                        queue.append(segment[0] if segment[1] == node else segment[1])
                        segments.remove(segment)
        figures.add(frozenset(figure_segments))
    polygons = sum(is_polygon(graph, start) for start in figures if is_polygon(graph, start))
    return len(figures), polygons

lines = sys.stdin.readlines()
segments = parse_input(lines)
figures, polygons = count_figures_and_polygons(segments)
print(figures, polygons)