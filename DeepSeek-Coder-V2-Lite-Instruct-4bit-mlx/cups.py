def extract_cup_info(messages):
    cups = []
    for msg in messages:
        tokens = msg.split()
        if len(tokens) == 2:
            color, radius = tokens[0], int(tokens[1])
        else:
            radius, color = int(tokens[0]), tokens[1]
        cups.append((color, radius))
    return cups

def main():
    N = int(input())
    messages = [input().strip() for _ in range(N)]
    cups = extract_cup_info(messages)
    cups.sort(key=lambda x: x[1])
    for color, _ in cups:
        print(color)

if __name__ == "__main__":
    main()