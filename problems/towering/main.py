def main():
    while True:
        try:
            boxes = list(map(int, input().split()))
            tower1_height = max(boxes)
            boxes.remove(tower1_height)
            tower2_height = sum(boxes) - tower1_height
            tower1 = []
            tower2 = []
            
            for box in reversed(sorted(boxes)):
                if sum(tower1) + box <= tower1_height:
                    tower1.append(box)
                else:
                    tower2.append(box)
            
            print(" ".join(map(str, sorted(tower1, reverse=True))), " ".join(map(str, sorted(tower2, reverse=True))))
        except EOFError:
            break

if __name__ == "__main__":
    main()