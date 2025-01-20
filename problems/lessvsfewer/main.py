def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    p = int(data[1])
    
    noun_types = {}
    for i in range(n):
        noun, typ = data[2 + i * 2], data[3 + i * 2]
        noun_types[noun] = typ
    
    phrases = data[2 + n * 2:]
    for phrase in phrases:
        words = phrase.split()
        correct = True
        for word in words:
            if '<' in word and '>' in word:
                noun = word[1:-1]
                if noun_types.get(noun, '') == ('c' if word.endswith('c') else 'm'):
                    continue
                else:
                    correct = False
                    break
        print("Correct!" if correct else "Not on my watch!")

if __name__ == "__main__":
    main()