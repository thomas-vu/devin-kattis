def mirror_image(R, C, image):
    mirrored_image = []
    for row in image:
        mirrored_row = row[::-1]
        mirrored_image.append(mirrored_row)
    for row in reversed(image):
        mirrored_image.append(row[::-1])
    return mirrored_image

def main():
    T = int(input())
    for t in range(1, T + 1):
        R, C = map(int, input().split())
        image = [input() for _ in range(R)]
        mirrored_image = mirror_image(R, C, image)
        print("Test", t)
        for row in mirrored_image:
            print(row)

if __name__ == "__main__":
    main()