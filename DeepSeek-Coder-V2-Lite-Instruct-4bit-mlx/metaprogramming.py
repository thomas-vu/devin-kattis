d = {}
while True:
    try:
        cmd = input().split()
        if cmd[0] == 'define':
            i, x = int(cmd[1]), cmd[2]
            d[x] = i
        elif cmd[0] == 'eval':
            x, y, z = cmd[1], cmd[2], cmd[3]
            if x not in d or z not in d:
                print('undefined')
            else:
                ix, iz = d[x], d[z]
                if y == '<':
                    print(ix < iz)
                elif y == '>':
                    print(ix > iz)
                elif y == '=':
                    print(ix == iz)
    except EOFError:
        break