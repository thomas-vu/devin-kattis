def number_to_words(num):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred", "sevenhundred", "eighthundred", "ninehundred"]

    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 11]
    elif num < 100:
        return tens[num // 10 - 1] + ("" if num % 10 == 0 else ones[num % 10])
    else:
        return hundreds[num // 100 - 1] + (number_to_words(num % 100) if num % 100 != 0 else "")

def main():
    N = int(input())
    words = [input().strip() for _ in range(N)]
    idx = words.index("$")
    
    min_length = float('inf')
    min_words = []
    
    for i in range(1, 1000):
        words_copy = words.copy()
        words_copy[idx] = str(i)
        sentence = " ".join(words_copy)
        if len(sentence.replace(" ", "")) == i:
            if min_length > i:
                min_length = i
                min_words = words_copy.copy()
    
    print(" ".join(min_words))

if __name__ == "__main__":
    main()