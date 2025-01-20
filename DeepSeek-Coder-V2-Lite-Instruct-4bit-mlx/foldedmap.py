def min_tiles(A_r, A_c, T_r, T_c):
    garden = [input().strip() for _ in range(A_r)]
    count = 0
    
    for i in range(0, A_r, T_r):
        for j in range(0, A_c, T_c):
            tile_covered = False
            for k in range(i, min(i + T_r, A_r)):
                for l in range(j, min(j + T_c, A_c)):
                    if garden[k][l] == 'X':
                        tile_covered = True
                        break
                if tile_covered:
                    break
            if tile_covered:
                count += 1
    
    print(count)

# Read input until EOF
while True:
    try:
        A_r, A_c, T_r, T_c = map(int, input().split())
        min_tiles(A_r, A_c, T_r, T_c)
    except EOFError:
        break