def can_finish(n, prerequisites):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    in_degree = [0] * n
    
    for i, prereqs in enumerate(prerequisites):
        m_i = prereqs[0]
        for j in range(1, len(preqs)):
            course = prereqs[j] - 1
            graph[course].append(i)
            in_degree[i] += 1
    
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    visited = set()
    semesters = []
    
    while queue:
        semester_size = len(queue)
        courses_in_semester = []
        
        for _ in range(semester_size):
            course = queue.popleft()
            courses_in_semester.append(course + 1)
            visited.add(course)
            
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        semesters.append(courses_in_semester)
    
    if len(visited) == n:
        print("Mogulegt!")
        print(len(semesters))
        for semester in semesters:
            print(f"{len(semester)} {' '.join(map(str, semester))}")
    else:
        print("Omogulegt!")

# Example usage:
n = int(input())
prerequisites = [list(map(int, input().split())) for _ in range(n)]
can_finish(n, prerequisites)