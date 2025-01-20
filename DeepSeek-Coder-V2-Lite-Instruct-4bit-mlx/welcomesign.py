def main():
    r, c = map(int, input().split())
    words = [input() for _ in range(r)]
    
    # Determine the maximum length of words
    max_word_length = 0
    for word in words:
        max_word_length = max(max_word_length, len(word))
    
    # Adjust the words to have equal length by padding with spaces
    for i in range(r):
        word_length = len(words[i])
        padding = (c - word_length) // 2
        words[i] = ' ' * padding + words[i] + ' ' * (c - word_length - padding)
    
    # Balance the left and right spaces for each row
    for i in range(r):
        word = words[i]
        left_space = (c - len(word)) // 2
        right_space = c - len(word) - left_space
        
        if i % 2 == 0:
            # For odd rows, make left space less than right space
            words[i] = ' ' * (left_space + 1) + word + ' ' * right_space
        else:
            # For even rows, make left space greater than right space
            words[i] = ' ' * left_space + word + ' ' * (right_space + 1)
    
    # Output the final arrangement of words on the sign
    for word in words:
        print(word)

if __name__ == "__main__":
    main()