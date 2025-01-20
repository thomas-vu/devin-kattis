import sys
from math import isclose

def read_ints():
    return list(map(int, input().split()))

def read_floats():
    return list(map(float, input().split()))

def read_links(l):
    links = []
    for _ in range(l):
        s, t, p = read_ints()
        links.append((s, t, p))
    return links

def strength_after_time(strengths, links, t):
    n = len(strengths)
    strength_values = strengths.copy()
    
    for _ in range(t):
        new_strengths = [0.0] * n
        for s, t, p in links:
            new_strengths[t] += strength_values[s] * p
            new_strengths[s] += strength_values[t] * (1 - p)
        
        strength_values = new_strengths
    
    return strength_values

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        N, l, t = read_ints()
        strengths = read_floats()
        links = read_links(l)
        
        final_strengths = strength_after_time(strengths, links, t)
        
        min_strength = min(final_strengths)
        results.append("{:.9f}".format(min_strength))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()