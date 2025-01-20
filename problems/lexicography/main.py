def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def kth_anagram(word, K):
    from collections import Counter
    counter = Counter(word)
    letters = list(word)
    letters.sort()
    
    result = []
    n = len(letters)
    while n > 0:
        fact = factorial(n - 1)
        index = (K - 1) // fact
        result.append(letters[index])
        letters.pop(index)
        K %= fact
        n -= 1
    
    return ''.join(result)

while True:
    line = input()
    if line == "# 0":
        break
    word, K = line.split()
    K = int(K)
    print(kth_anagram(word, K))