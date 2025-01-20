def main():
    n = int(input())
    colors = list(map(int, input().split()))
    
    # Check if the number of unique colors is greater than 1
    if len(set(colors)) == 1:
        print("IMPOSSIBLE")
        return
    
    # Create a list to store the instructions
    instructions = []
    
    # Iterate over the colors and find the first occurrence of each color
    for color in set(colors):
        start = colors.index(color)
        end = n - list(reversed(colors)).index(color) - 1
        instructions.append((start + 1, end + 1, color))
    
    # Output the number of instructions and each instruction
    print(len(instructions))
    for l, r, c in instructions:
        print(l, r, c)

if __name__ == "__main__":
    main()