def main():
    n, t = map(int, input().split())
    prescriptions = []
    
    for _ in range(n):
        d, typ, k = input().split()
        prescriptions.append((int(d), typ, int(k)))
    
    in_store = [pres for pres in prescriptions if pres[1] == 'S']
    remote = [pres for pres in prescriptions if pres[1] == 'R']
    
    in_store.sort(key=lambda x: (x[0], x[2]))
    remote.sort(key=lambda x: (x[0], x[2]))
    
    in_store_time = 0
    remote_time = 0
    in_store_count = len(in_store)
    remote_count = len(remote)
    
    for i in range(min(t, len(in_store))):
        in_store_time += in_store[i][0] + sum(pres[2] for pres in in_store[:i+1])
    
    remote_time = sum(pres[2] for pres in remote) + sum(pres[2] for pres in in_store[:t])
    total_time = sum(pres[2] for pres in remote) + sum(pres[2] for pres in in_store[:t])
    
    if remote_count > 0:
        remote_avg = remote_time / remote_count
    else:
        remote_avg = 0
    
    if in_store_count > 0:
        in_store_avg = in_store_time / in_store_count
    else:
        in_store_avg = 0
    
    print("{:.6f} {:.6f}".format(in_store_avg, remote_avg))

if __name__ == "__main__":
    main()