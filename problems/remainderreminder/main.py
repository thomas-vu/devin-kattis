def main():
    a, b, c, d, e, f, g = map(int, input().split())
    
    def box_volume(x, y):
        return x * y * z
    
    def cut_box(x, y):
        return (a - 2 * x) * (b - 2 * y)
    
    def find_boxes(x, y):
        return (a // x) * (b // y), (a // y) * (b // x)
    
    max_books = 0
    min_books = float('inf')
    
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            z = cut_box(x, y)
            if z > 0:
                box1 = find_boxes(x, y)
                books1 = (c - 407) * box1[0] + d
                books2 = (e - 409) * box1[1] + f
                books3 = g - books2
                
                if books1 == 0 and books2 == 0 and books3 == 0:
                    max_books = max(max_books, z)
                    min_books = min(min_books, z)
    
    print(max_books)

main()