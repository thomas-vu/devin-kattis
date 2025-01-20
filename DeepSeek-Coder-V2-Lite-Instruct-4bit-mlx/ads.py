H, W = map(int, input().split())
page = [input() for _ in range(H)]

def find_images(page, H, W):
    images = []
    for i in range(H):
        for j in range(W):
            if page[i][j] == '+':
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < H and 0 <= nj < W and page[ni][nj] == '+':
                        for dii, djj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nni, nnj = ni + dii, nj + djj
                            if 0 <= nni < H and 0 <= nnj < W and page[nni][nnj] == '+':
                                if (nni, nnj) not in [(ni - di, nj - dj), (ni + dii, nj + djj)]:
                                    break
                        else:
                            top_left = (ni, nj)
                            for d in range(1, min(H - top_left[0], W - top_left[1])):
                                valid = True
                                for x in range(top_left[0], top_left[0] + d):
                                    for y in range(top_left[1], top_left[1] + d):
                                        if page[x][y] not in ['+', ' ', '!', '.', '?', ',']:
                                            valid = False
                                            break
                                    if not valid:
                                        break
                                if valid:
                                    bottom_right = (top_left[0] + d, top_left[1] + d)
                                    images.append((top_left, bottom_right))
                                else:
                                    break
    return images

def remove_ads(page, H, W):
    images = find_images(page, H, W)
    for top_left, bottom_right in images:
        for i in range(top_left[0], bottom_right[0] + 1):
            for j in range(top_left[1], bottom_right[1] + 1):
                page[i][j] = ' '
    return page

# Process the web page
page = [list(row) for row in page]
remove_ads(page, H, W)

# Output the result
for row in page:
    print(''.join(row))