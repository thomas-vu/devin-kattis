def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    ll = int(data[0])
    m = int(data[1])
    
    lawnmovers = []
    
    for i in range(2, 2 + m):
        name, p, c, t, r = data[i].split(',')
        p = int(p)
        c = int(c)
        t = int(t)
        r = int(r)
        lawnmovers.append((name, p, c, t, r))
    
    valid_mowers = []
    
    for name, p, c, t, r in lawnmovers:
        total_minutes = 0
        weeks = 0
        while total_minutes < ll:
            if total_minutes + c * t >= ll:
                weeks += 1
                total_minutes = min(total_minutes + c * t - ll, total_minutes + c * t)
            else:
                total_minutes += c * t - r * (c * t) // ll
            if weeks >= T:
                valid_mowers.append((name, p))
                break
    
    if not valid_mowers:
        print("no such mower")
    else:
        cheapest = min(valid_mowers, key=lambda x: x[1])
        result = [name for name, price in valid_mowers if price == cheapest[1]]
        print(' '.join(result))

if __name__ == "__main__":
    main()