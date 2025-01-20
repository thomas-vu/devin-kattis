def min_servers(n, k, requests):
    servers = []
    for request in requests:
        added = False
        for i in range(len(servers)):
            if servers[i] <= request:
                servers[i] = request + 1000
                added = True
                break
        if not added:
            servers.append(request + 1000)
    return len(servers)

n, k = map(int, input().split())
requests = [int(input()) for _ in range(n)]
print(min_servers(n, k, requests))