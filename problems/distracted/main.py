def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    L = int(data[1])
    
    statuses = {}
    links = {}
    
    for i in range(2, N + 2):
        name, status = data[i].split()
        statuses[name] = status
    
    for i in range(N + 2, N + L + 2):
        src, _, dst = data[i].partition('->')
        links[src] = dst
    
    married_looking_at_unmarried = False
    
    for person, link in links.items():
        if statuses[person] == 'm' and statuses[link] == 'u':
            married_looking_at_unmarried = True
            break
    
    if married_looking_at_unmarried:
        print(1)
    else:
        all_known = all(status in {'m', 'u'} for status in statuses.values())
        if all_known and not married_looking_at_unmarried:
            print(0)
        else:
            print('?')

if __name__ == "__main__":
    main()