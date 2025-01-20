def main():
    while True:
        r, c = map(int, input().split())
        if r == 0 and c == 0:
            break
        
        matrix = [input().strip() for _ in range(r)]
        
        # Create a list of columns as strings
        columns = ['' for _ in range(c)]
        for row in matrix:
            for i, char in enumerate(row):
                columns[i] += char
        
        # Sort the columns lexicographically, ignoring case
        sorted_columns = sorted(columns, key=lambda x: x.lower())
        
        # Print the sorted columns
        for col in sorted_columns:
            print(col)
        
        # Print a blank line between each pair of adjacent output blocks
        print()

if __name__ == "__main__":
    main()