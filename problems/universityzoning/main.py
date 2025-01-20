def min_steps(R, C, F, S, G, faculties, students):
    from collections import deque
    
    # Create a grid to store the number of students in each faculty's cell
    grid = [[0] * (C + 1) for _ in range(R + 1)]
    faculty_students = [[] for _ in range(F + 1)]
    
    # Populate the grid with students' positions and count them
    for student in students:
        r, c, _, f = student
        faculty_students[f].append((r, c))
        grid[r][c] += 1
    
    # Define the targets for each faculty
    targets = [0] * (F + 1)
    for i, t in enumerate(targets):
        targets[i] = int(input())
    
    # BFS to calculate the minimum steps for each faculty's students to reach their assigned cells
    def bfs(start_points):
        visited = set()
        queue = deque([(0, p[0], p[1]) for p in start_points])
        while queue:
            steps, r, c = queue.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if grid[r][c] > 0:
                for faculty in range(1, F + 1):
                    if (r, c) in faculties[faculty]:
                        grid[r][c] -= 1
                continue
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 1 <= nr <= R and 1 <= nc <= C:
                    queue.append((steps + 1, nr, nc))
        return steps
    
    # Calculate the minimum steps for each faculty's students to reach their assigned cells
    min_steps = 0
    for i in range(1, F + 1):
        if len(faculty_students[i]) > 0:
            min_steps += bfs(faculty_students[i])
    
    return min_steps

# Read input and process the problem
R, C, F, S, G = map(int, input().split())
faculties = [[] for _ in range(F + 1)]
for i in range(1, F + 1):
    K = int(input())
    for _ in range(K):
        r, c = map(int, input().split())
        faculties[i].append((r, c))
students = [list(map(int, input().split())) for _ in range(S)]
print(min_steps(R, C, F, S, G, faculties, students))