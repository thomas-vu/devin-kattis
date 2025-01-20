def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    def two_digit(num):
        if num < 10:
            return ones[num]
        elif 10 <= num < 20:
            return teens[num - 10]
        else:
            return tens[num // 10] + ("" if num % 10 == 0 else "-" + ones[num % 10])
    
    if n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    elif 100 > n >= 20:
        return tens[n // 10] + ("" if n % 10 == 0 else "-" + ones[n % 10])
    elif n == 100:
        return "one hundred"
    
def replace_numbers(line):
    words = line.split()
    new_words = []
    for word in words:
        if word.isdigit():
            num = int(word)
            if 0 <= num <= 99:
                new_words.append(number_to_words(num))
            else:
                new_words.append(word)
        else:
            new_words.append(word)
    return ' '.join(new_words)

import sys
for line in sys.stdin:
    print(replace_numbers(line.strip()))