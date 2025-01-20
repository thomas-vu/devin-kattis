def is_valid(word, guess, feedback):
    for i in range(len(feedback)):
        if feedback[i] == 'G' and word[i] != guess[i]:
            return False
        if feedback[i] == 'Y' and (word[i] == guess[i] or guess[i] not in word):
            return False
        if feedback[i] == '-' and (word[i] in word[:i] or word[i] in word[i+1:]):
            return False
    return True

def main():
    N, W = map(int, input().split())
    guesses = [input().strip() for _ in range(N)]
    words = [input().strip() for _ in range(W)]
    
    for guess, feedback in guesses:
        words = [word for word in words if is_valid(word, guess, feedback)]
    
    for valid_word in words:
        print(valid_word)

if __name__ == "__main__":
    main()