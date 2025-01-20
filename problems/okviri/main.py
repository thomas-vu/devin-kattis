def create_frame(word):
    frames = []
    for i, char in enumerate(word):
        if (i + 1) % 3 == 0:
            frame = [
                f"..*..",
                f".{char}*.*.",
                f"*{char}.*.",
                f".{char}*.*.",
                f"..*.."
            ]
        else:
            frame = [
                f"..#..",
                f".{char}#.",
                f"#{char}#",
                f".{char}#.",
                f"..#.."
            ]
        frames.append(frame)
    
    for i in range(5):
        line = ""
        for j in range(len(word)):
            if i < len(frames[j]):
                line += frames[j][i]
        print(line)

word = input()
create_frame(word)