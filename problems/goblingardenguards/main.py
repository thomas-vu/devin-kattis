def main():
    g = int(input())
    goblins = [tuple(map(int, input().split())) for _ in range(g)]
    m = int(input())
    sprinklers = [tuple(map(int, input().split())) for _ in range(m)]
    
    soaked = set()
    for x, y, r in sprinklers:
        for i in range(g):
            gx, gy = goblins[i]
            if (gx - x)**2 + (gy - y)**2 <= r**2:
                soaked.add(i)
    
    remaining_goblins = g - len(soaked)
    print(remaining_goblins)

if __name__ == "__main__":
    main()