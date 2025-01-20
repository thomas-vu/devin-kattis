def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    A = int(data[0])
    names = data[1:A+1]
    B = int(data[A+1])
    nicknames = data[A+2:]
    
    for nickname in nicknames:
        count = 0
        for name in names:
            if name.startswith(nickname):
                count += 1
        print(count)

if __name__ == "__main__":
    main()