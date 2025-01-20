def draw_alkanol(c):
    if c == 1:
        print("H")
        print("|")
        print("H-C-OH")
        print("|")
        print("H")
    elif c == 2:
        print("H H")
        print(" | | ")
        print("H-C-C-OH")
        print(" | | ")
        print("H H")

# Example usage:
draw_alkanol(1)
draw_alkanol(2)