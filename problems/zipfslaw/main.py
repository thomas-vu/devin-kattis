import re
from collections import defaultdict

def main():
    while True:
        try:
            n = int(input())
            text = []
            while True:
                line = input().lower()
                if line == "endoftext":
                    break
                text.append(line)
            word_count = defaultdict(int)
            for line in text:
                words = re.findall(r'\b\w+\b', line)
                for word in words:
                    word_count[word] += 1
            result = [word for word, cnt in word_count.items() if cnt == n]
            result.sort()
            for word in result:
                print(word)
            if not result and text:
                print("There is no such word.")
            print()
        except EOFError:
            break

if __name__ == "__main__":
    main()