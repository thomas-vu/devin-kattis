def main():
    while True:
        line = input()
        if line == "0.0 0":
            break
        d, N = map(float, line.split())
        hives = [tuple(map(float, input().split())) for _ in range(int(N))]
        
        sour_count = 0
        sweet_count = 0
        
        for i in range(len(hives)):
            fight = False
            for j in range(i + 1, len(hives)):
                if (hives[i][0] - hives[j][0])**2 + (hives[i][1] - hives[j][1])**2 <= d**2:
                    fight = True
                    break
            if fight:
                sour_count += 1
            else:
                sweet_count += 1
        
        print(f"{sour_count} sour, {sweet_count} sweet")

if __name__ == "__main__":
    main()