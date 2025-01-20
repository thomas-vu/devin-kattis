def can_be_ordered(packages, dependencies):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    in_degree = {package: 0 for package in packages}
    
    # Build the graph and calculate in-degree counts
    for package, dependencies_list in dependencies.items():
        for dependency in dependencies_list:
            graph[dependency].append(package)
            in_degree[package] += 1
    
    # Topological sort using Kahn's algorithm
    queue = deque([package for package in packages if in_degree[package] == 0])
    ordered = []
    
    while queue:
        package = queue.popleft()
        ordered.append(package)
        
        for dependent in graph[package]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    return ordered if len(ordered) == len(packages) else None

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        packages = {}
        dependencies = {}
        
        for _ in range(n):
            line = input().split()
            package_name = line[0]
            dependencies_list = line[1:] if len(line) > 1 else []
            
            packages[package_name] = dependencies_list
            dependencies[package_name] = []
            
            for dep in dependencies_list:
                if dep not in packages:
                    packages[dep] = []
            
            for dep in dependencies_list:
                dependencies[package_name].append(dep)
        
        ordered = can_be_ordered(packages.keys(), dependencies)
        
        if ordered:
            print("\n".join(ordered))
        else:
            print("cannot be ordered")
        print()

if __name__ == "__main__":
    main()