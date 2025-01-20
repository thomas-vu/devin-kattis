def find_player(K, questions):
    player = K - 1  # Start with the player holding the box
    for time, answer in questions:
        if answer == 'N':  # Skip the question
            player = (player + 1) % 8
        elif answer == 'T':  # Answer correctly
            player = (player + 1) % 8
        elif answer == 'P':  # Skip the question
            player = (player + 1) % 8
        else:
            break  # Invalid answer, stop the process
    return player + 1  # Convert to 1-based index for output

# Main function to read input and call the solution
def main():
    K = int(input())
    N = int(input())
    questions = [tuple(input().split()) for _ in range(N)]
    questions = [(int(time), answer) for time, answer in questions]
    result = find_player(K, questions)
    print(result)

if __name__ == "__main__":
    main()