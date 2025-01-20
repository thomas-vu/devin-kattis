def can_form_server(a, b):
    return (a[0] == 'J' or b[0] == 'J') and (a[1] == 'J' or b[1] == 'J') and (a[2] == 'J' or b[2] == 'J')

def max_servers(n, servers):
    count = 0
    for i in range(n):
        for j in range(i, n):
            if can_form_server(servers[i], servers[j]):
                count += 1
    return count

n = int(input())
servers = [input().strip() for _ in range(n)]
print(max_servers(n, servers))