import sys
from itertools import permutations

def read_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def calculate_penalty(order):
    time = 0
    ac_count = 0
    for problem in order:
        time += problem
        if time <= 300:
            ac_count += 1
        else:
            break
    penalty = sum(filter(lambda x: x <= 300, order))
    return ac_count, penalty

N, p = read_ints()
problem_times = read_ints()

best_ac = 0
best_penalty = float('inf')

for order in permutations(problem_times):
    ac_count, penalty = calculate_penalty(order)
    if ac_count > best_ac or (ac_count == best_ac and penalty < best_penalty):
        best_ac = ac_count
        best_penalty = penalty

print(best_ac, best_penalty)