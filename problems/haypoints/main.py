m, n = map(int, input().split())
word_values = {}
for _ in range(m):
    word, value = input().split()
    word_values[word] = int(value)

for _ in range(n):
    total_salary = 0
    while True:
        line = input().split()
        for word in line:
            if word.isalpha():  # Ensure the word is alphabetic before checking for dictionary presence
                total_salary += word_values.get(word, 0)
        if '.' in line:  # Stop condition for reading job descriptions
            break
    print(total_salary)