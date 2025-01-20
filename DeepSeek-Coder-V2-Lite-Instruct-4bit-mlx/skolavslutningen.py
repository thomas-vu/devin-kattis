def main():
    N, M, K = map(int, input().split())
    classes = [input() for _ in range(N)]
    
    # Initialize the number of unique hat colors to 0
    max_hats = 0
    
    # Iterate through each column and check the classes in that column
    for col in range(M):
        unique_classes = set()
        # Collect all classes in the current column
        for row in range(N):
            unique_classes.add(classes[row][col])
        # The number of unique hat colors for this column is the number of unique classes
        max_hats += len(unique_classes)
    
    print(max_hats)

if __name__ == "__main__":
    main()