n = int(input())
for _ in range(n):
    memed_sentence = input()
    unmemed_sentence = ""
    make_uppercase = True
    for char in memed_sentence:
        if char.isalpha():
            if make_uppercase:
                unmemed_sentence += char.upper()
            else:
                unmemed_sentence += char.lower()
            make_uppercase = not make_uppercase
        else:
            unmemed_sentence += char
    print(unmemed_sentence)