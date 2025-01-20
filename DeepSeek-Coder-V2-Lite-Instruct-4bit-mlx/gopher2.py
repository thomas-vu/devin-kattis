Here is the complete, runnable solution in Python 3 for the given problem:

```python
import math

def time_to_reach(gx, gy, hx, hy, s):
    distance = math.sqrt((hx - gx)**2 + (hy - gy)**2)
    return distance / s

def main():
    while True:
        try:
            n, m, s, v = map(int, input().split())
            gophers = [tuple(map(float, input().split())) for _ in range(n)]
            holes = [tuple(map(float, input().split())) for _ in range(m)]
            
            vulnerable_gophers = set()
            
            for gx, gy in gophers:
                min_time = float('inf')
                for hx, hy in holes:
                    time_to_hole = time_to_reach(gx, gy, hx, hy, s)
                    if time_to_hole < min_time:
                        min_time = time_to_hole
                
                if min_time * v >= time_to_reach(gx, gy, 100.0, 100.0, s):
                    vulnerable_gophers.add((gx, gy))
            
            print(len(vulnerable_gophers))
        except EOFError:
            break

if __name__ == "__main__":
    main()