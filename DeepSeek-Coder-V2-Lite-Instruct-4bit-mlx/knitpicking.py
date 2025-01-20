def min_socks_to_draw(n, sock_data):
    from collections import defaultdict
    
    left_socks = defaultdict(int)
    right_socks = defaultdict(int)
    
    for _ in range(n):
        sock_type, fit, count = input().split()
        count = int(count)
        
        if fit == 'left':
            left_socks[sock_type] += count
        elif fit == 'right':
            right_socks[sock_type] += count
        else:  # fit == 'any'
            left_socks[sock_type] += count
            right_socks[sock_type] += count
    
    min_draw = float('inf')
    for sock_type in left_socks:
        if sock_type in right_socks:
            min_draw = min(min_draw, left_socks[sock_type] + right_socks[sock_type])
    
    return min_draw if min_draw != float('inf') else "impossible"

# Read the number of groups of identical socks
n = int(input())
print(min_socks_to_draw(n, []))