def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        boxes = {}
        for _ in range(n):
            x1, y1, x2, y2, size = input().split()
            boxes[(float(x1), float(y1)), (float(x2), float(y2))] = size
        
        m = int(input())
        peanuts = []
        for _ in range(m):
            x, y, peanut_size = input().split()
            peanuts.append((float(x), float(y), peanut_size))
        
        for peanut in peanuts:
            x, y = peanut[:2]
            found_box = None
            for box in boxes:
                x1, y1 = box[0]
                x2, y2 = box[1]
                if x1 <= x <= x2 and y1 <= y <= y2:
                    found_box = box
                    break
            if found_box is None:
                print(peanut[2], 'floor')
            elif boxes[found_box] == peanut[2]:
                print(peanut[2], 'correct')
            else:
                print(peanut[2], boxes[found_box])
        print()

if __name__ == "__main__":
    main()