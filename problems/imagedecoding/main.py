def decode_image(scanlines):
    decoded = []
    for scanline in scanlines:
        pixels = ''
        i = 0
        while i < len(scanline):
            if scanline[i] == '.':
                pixels += '.' * int(scanline[i+1])
                i += 2
            elif scanline[i] == '#':
                pixels += '#' * int(scanline[i+1])
                i += 2
        decoded.append(pixels)
    return decoded

def main():
    images = []
    while True:
        n = int(input())
        if n == 0:
            break
        scanlines = [input() for _ in range(n)]
        images.append(scanlines)
    
    decoded_images = []
    for image in images:
        try:
            decoded_image = decode_image(image)
            decoded_images.append('\n'.join(decoded_image))
        except:
            decoded_images.append('Error decoding image')
    
    for i in range(len(decoded_images)):
        if decoded_images[i] != 'Error decoding image':
            print(f'Image {i+1}')
            print('\n'.join(decoded_images[i]))
            if i != len(decoded_images) - 1:
                print()
        else:
            if i != len(decoded_images) - 1:
                print('Error decoding image')
            else:
                print(decoded_images[i])

if __name__ == "__main__":
    main()