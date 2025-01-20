import sys
from collections import defaultdict, deque

class Employee:
    def __init__(self, name, speed, supervisor):
        self.name = name
        self.speed = float(speed)
        self.supervisor = supervisor

def read_input():
    n = int(sys.stdin.readline().strip())
    employees = {}
    for _ in range(n):
        name, speed, supervisor = sys.stdin.readline().strip().split()
        employees[name] = Employee(name, speed, supervisor)
    return employees

def build_tree(employees):
    tree = defaultdict(list)
    for employee in employees.values():
        if employee.supervisor != "CEO":
            tree[employee.supervisor].append(employee)
    return tree

def dfs(tree, employee):
    min_speed = employee.speed
    for subordinate in tree[employee.name]:
        min_speed = min(min_speed, dfs(tree, subordinate))
    return min_speed

def main():
    employees = read_input()
    tree = build_tree(employees)
    
    # Topological sort to ensure we process employees in a valid order
    processing_order = deque([employees["CEO"]])
    for employee in employees.values():
        if employee.supervisor == "CEO":
            processing_order.append(employee)
    
    teams = []
    while processing_order:
        employee = processing_order.popleft()
        if tree[employee.name]:
            min_subordinate_speed = float('inf')
            for subordinate in tree[employee.name]:
                min_subordinate_speed = min(min_subordinate_speed, subordinate.speed)
            if min_subordinate_speed > employee.speed:  # Ensure the supervisor is not slower than any subordinate
                processing_order.append(employees[employee.name])  # Continue to process this employee
            else:
                teams.append((employee, min_subordinate_speed))
        else:
            teams.append((employee, employee.speed))
    
    num_teams = len(teams)
    total_speed = sum(employee.speed for employee, _ in teams)
    average_speed = total_speed / num_teams if num_teams > 0 else 0
    
    print(num_teams)
    print("{:.6f}".format(average_speed))

if __name__ == "__main__":
    main()