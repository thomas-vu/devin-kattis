def parse_ascii(art):
    digits = {
        '0': [
            "xxxxx",
            "x...x",
            "x...x",
            "x...x",
            "x...x",
            "xxxxx"
        ],
        '1': [
            "....x",
            "..x..",
            "..x..",
            "..x..",
            "..x..",
            "..x.."
        ],
        '2': [
            "xxxxx",
            "....x",
            "....x",
            "xxxx.",
            "....x",
            "xxxxx"
        ],
        '3': [
            "xxxxx",
            "....x",
            "....x",
            "xxxx.",
            "....x",
            "xxxxx"
        ],
        '4': [
            "x...x",
            "x...x",
            "xxxxx",
            "....x",
            "....x",
            "....x"
        ],
        '5': [
            "xxxxx",
            "x....",
            "x....",
            "xxxx.",
            "....x",
            "xxxxx"
        ],
        '6': [
            "xxxxx",
            "x....",
            "x....",
            "xxxx.",
            "x...x",
            "xxxxx"
        ],
        '7': [
            "xxxxx",
            "....x",
            "....x",
            "....x",
            "....x",
            "....x"
        ],
        '8': [
            "xxxxx",
            "x...x",
            "x...x",
            "xxxx.",
            "x...x",
            "xxxxx"
        ],
        '9': [
            "xxxxx",
            "x...x",
            "x...x",
            "xxxx.",
            "....x",
            "xxxxx"
        ],
        '+': [
            ".....",
            "..x..",
            "..x..",
            "xxxxx",
            "..x..",
            "..x.."
        ]
    }
    
    num_width = 5
    result = ""
    for i in range(7):
        row = ""
        for char in art[i]:
            if char == '.':
                row += '0'
            else:
                row += '1'
        result += chr(int(row, 2) + ord('0'))
    return result

# Input reading
art = [input() for _ in range(7)]

# Output the result of addition
print("".join([str(int(parse_ascii(art))) for _ in range(7)]))