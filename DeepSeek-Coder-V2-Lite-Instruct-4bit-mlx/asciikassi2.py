def print_box(n):
    if n == 0:
        print("x")
        return
    
    # Top half of the box
    for i in range(n):
        spaces = ' ' * (i)
        if i == 0:
            print(spaces + "x")
        else:
            slash = '/' if i == n - 1 else ' '
            backslash = '\\' if i == n - 1 else ' '
            print(spaces + "x" + slash * (i) + backslash * (i))
    
    # Bottom half of the box mirrored top half
    for i in range(n-2, -1, -1):
        spaces = ' ' * i
        slash = '/' if i == 0 else ' '
        backslash = '\\' if i == 0 else ' '
        print(spaces + "x" + slash * (i) + backslash * (i))

# Read the input
n = int(input())
print_box(n)