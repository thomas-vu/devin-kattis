def is_östgötska(sentence):
    words = sentence.split()
    count_ä = 0
    for word in words:
        if 'ae' in word:
            count_ä += 1
    return count_ä / len(words) >= 0.4

sentence = input()
if is_östgötska(sentence):
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")