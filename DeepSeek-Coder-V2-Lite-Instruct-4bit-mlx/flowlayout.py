def main():
    while True:
        max_width = int(input())
        if max_width == 0:
            break
        
        width = 0
        height = 0
        current_row_width = 0
        max_height_in_row = 0
        
        while True:
            w, h = map(int, input().split())
            if w == -1 and h == -1:
                break
            
            if current_row_width + w > max_width:
                width = max(width, current_row_width)
                height += max_height_in_row
                current_row_width = w
                max_height_in_row = h
            else:
                current_row_width += w
                max_height_in_row = max(max_height_in_row, h)
        
        width = max(width, current_row_width)
        height += max_height_in_row
        
        print(f"{width} x {height}")

if __name__ == "__main__":
    main()