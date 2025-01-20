H, W, N, M = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(H)]
kernel = [list(map(int, input().split())) for _ in range(N)]

def convolve(image, kernel):
    result = [[0] * (W - M + 1) for _ in range(H - N + 1)]
    for i in range(H - N + 1):
        for j in range(W - M + 1):
            value = 0
            for k in range(N):
                for l in range(M):
                    value += image[i + k][j + l] * kernel[N - 1 - k][M - 1 - l]
            result[i][j] = value
    return result

result_image = convolve(image, kernel)
for row in result_image:
    print(' '.join(map(str, row)))