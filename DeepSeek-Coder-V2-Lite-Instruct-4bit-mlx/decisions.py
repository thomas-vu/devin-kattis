import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

@lru_cache(maxsize=None)
def min_bdd_vertices(function, var_indices):
    if not var_indices:
        return 1
    
    var = var_indices[0]
    left_indices = [i for i in range(len(function)) if (i >> var) & 1 == 0]
    right_indices = [i for i in range(len(function)) if (i >> var) & 1 == 1]
    
    left_function = [function[i] for i in left_indices]
    right_function = [function[i] for i in right_indices]
    
    left_vertices = min_bdd_vertices(tuple(left_function), var_indices[1:])
    right_vertices = min_bdd_vertices(tuple(right_function), var_indices[1:])
    
    return 1 + left_vertices + right_vertices

n = int(input().strip())
function = list(map(int, input().strip().split()))
var_indices = tuple(range(n))

result = min_bdd_vertices(tuple(function), var_indices)
print(result)