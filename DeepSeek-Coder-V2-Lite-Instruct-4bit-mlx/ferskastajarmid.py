def main():
    n = int(input())
    memes = []
    
    for _ in range(n):
        name, controversiality, coolness = input().split()
        memes.append((name, int(controversiality), int(coolness)))
    
    memes.sort(key=lambda x: (-x[1], -x[2], x[0]))
    
    print(memes[0][0])

if __name__ == "__main__":
    main()