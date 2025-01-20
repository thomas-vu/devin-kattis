def can_clara_speak(word):
    elements = [
        'h', 'he', 'li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne',
        'na', 'mg', 'al', 'si', 'p', 's', 'cl', 'ar',
        'k', 'ca', 'sc', 'ti', 'v', 'cr', 'mn', 'fe', 'co', 'ni', 'cu', 'zn', 'ga', 'ge', 'as', 'se', 'br', 'kr',
        'rb', 'sr', 'y', 'zr', 'nb', 'mo', 'tc', 'ru', 'rh', 'pd', 'ag', 'cd', 'in', 'sn', 'sb', 'te', 'i', 'xe',
        'cs', 'ba', 'la', 'ce', 'pr', 'nd', 'pm', 'sm', 'eu', 'gd', 'tb', 'dy', 'ho', 'er', 'tm', 'yb', 'lu',
        'ac', 'th', 'pa', 'u', 'np', 'pu', 'am', 'cm', 'bk', 'cf', 'es', 'fm', 'md', 'no', 'lr'
    ]
    
    def is_speakable(word):
        if not word:
            return True
        for element in elements:
            if word.startswith(element):
                return is_speakable(word[len(element):])
        return False
    
    return is_speakable(word)

def main():
    T = int(input())
    for _ in range(T):
        word = input()
        if can_clara_speak(word):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()