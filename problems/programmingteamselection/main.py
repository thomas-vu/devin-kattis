def can_form_teams(pairs, students):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for a, b in pairs:
        graph[a].append(b)
        graph[b].append(a)
    
    color = {}
    def dfs(node, c=0):
        if node in color:
            return color[node] == c
        color[node] = c
        for neighbor in graph[node]:
            if not dfs(neighbor, 1 - c):
                return False
        return True
    
    for student in students:
        if student not in color:
            if not dfs(student):
                return "impossible"
    return "possible"

def main():
    while True:
        m = int(input())
        if m == 0:
            break
        pairs = []
        students = set()
        for _ in range(m):
            a, b = input().split()
            pairs.append((a, b))
            students.add(a)
            students.add(b)
        print(can_form_teams(pairs, students))

if __name__ == "__main__":
    main()