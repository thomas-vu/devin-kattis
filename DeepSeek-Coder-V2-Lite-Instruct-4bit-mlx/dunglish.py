def main():
    n = int(input())
    s = input().split()
    m = int(input())
    
    dictionary = {}
    for _ in range(m):
        d, e, c = input().split()
        dictionary[d] = (e, c)
    
    correct_translations = 0
    incorrect_translations = 0
    
    for word in s:
        if word in dictionary and dictionary[word][1] == "correct":
            correct_translations += 1
        elif word in dictionary and dictionary[word][1] == "incorrect":
            incorrect_translations += 1
    
    if correct_translations + incorrect_translations == n:
        if correct_translations == n:
            print(" ".join(dictionary[word][0] for word in s))
            print("correct")
        else:
            print(correct_translations)
            print("incorrect")
    else:
        print(correct_translations + incorrect_translations)
        if correct_translations == 0:
            print("incorrect")
        else:
            print("correct")

if __name__ == "__main__":
    main()