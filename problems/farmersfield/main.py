def can_kill_all_weeds(field, r):
    n = len(field)
    last_weed = -1
    
    for i in range(n):
        if field[i] == 'W':
            if not (i - r <= last_weed <= i + r):
                return "IMPOSSIBLE"
            last_weed = i
    
    if last_weed == -1:
        return "POSSIBLE"
    else:
        return can_kill_all_weeds(field[last_weed-r+1:], r)

def main():
    n = int(input())
    field = input()
    r = int(input())
    
    result = can_kill_all_weeds(field, r)
    print(result)

if __name__ == "__main__":
    main()