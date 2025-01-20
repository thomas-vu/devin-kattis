def find_rhyming_word(common_word, lists):
    for word in common_word.split():
        for ending in lists:
            if word.endswith(ending):
                return True
    return False

def check_phrases(common_word, lists, phrases):
    for phrase in phrases:
        words = phrase.split()
        if len(words) == 2 and (find_rhyming_word(words[0], lists) or find_rhyming_word(words[1], lists)):
            print('YES')
        elif len(words) == 3 and (find_rhyming_word(words[0], lists) or find_rhyming_word(words[1], lists) or find_rhyming_word(words[2], lists)):
            print('YES')
        else:
            print('NO')

# Read input
common_word = input().strip()
E = int(input().strip())
lists = []
for _ in range(E):
    list_of_endings = input().strip().split()
    lists.append(list_of_endings)
P = int(input().strip())
phrases = []
for _ in range(P):
    phrase = input().strip()
    phrases.append(phrase)

# Check and print results
check_phrases(common_word, lists, phrases)