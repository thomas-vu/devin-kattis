import math

def factstone_rating(year):
    word_size = 16 + (year - 1960) // 10 * 8
    n = word_size * 4
    while math.factorial(n) > (1 << word_size):
        n -= 1
    return n

while True:
    year = int(input())
    if year == 0:
        break
    print(factstone_rating(year))