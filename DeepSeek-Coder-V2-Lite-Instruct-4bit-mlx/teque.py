from collections import deque
import sys
input = sys.stdin.readline

t = deque()
n = int(input())
for _ in range(n):
    s, x = input().split()
    x = int(x)
    
    if s == 'push_back':
        t.append(x)
    elif s == 'push_front':
        t.appendleft(x)
    elif s == 'push_middle':
        mid = len(t) // 2
        t.insert(mid, x)
    elif s == 'get':
        print(t[x])