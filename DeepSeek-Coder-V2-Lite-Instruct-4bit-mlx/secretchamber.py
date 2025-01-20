def can_transform(translations, word1, word2):
    if len(word1) != len(word2):
        return False
    
    for a, b in zip(word1, word2):
        if (a, b) not in translations and (b, a) not in translations:
            return False
    return True

def main():
    m, n = map(int, input().split())
    translations = set()
    
    for _ in range(m):
        a, b = input().split()
        translations.add((a, b))
    
    for _ in range(n):
        word1, word2 = input().split()
        if can_transform(translations, word1, word2):
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()