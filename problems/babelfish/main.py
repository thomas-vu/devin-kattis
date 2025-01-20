def main():
    dictionary = {}
    
    while True:
        try:
            line = input()
            if not line:
                break
            english_word, foreign_word = line.split()
            dictionary[foreign_word] = english_word
        except EOFError:
            break
    
    while True:
        try:
            word = input()
            if word in dictionary:
                print(dictionary[word])
            else:
                print("eh")
        except EOFError:
            break

if __name__ == "__main__":
    main()