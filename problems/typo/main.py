n = int(input())
words = [input().strip() for _ in range(n)]

def is_typo(word, dictionary):
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        if new_word in dictionary:
            return True
    return False

typos = [word for word in words if is_typo(word, words)]

if typos:
    for typo in typos:
        print(typo)
else:
    print("NO TYPOS")