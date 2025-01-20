n = int(input())
categories = {}
for _ in range(n):
    category_info = input().split()
    category_name = category_info[0]
    num_words = int(category_info[1])
    words = category_info[2:]
    categories[category_name] = set(words)

statement = []
while True:
    try:
        line = input().split()
        statement.extend(line)
    except EOFError:
        break

word_count = {}
for word in statement:
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1

max_matches = -1
suggested_categories = []
for category, words in categories.items():
    matches = sum(word_count.get(w, 0) for w in words)
    if matches > max_matches:
        max_matches = matches
        suggested_categories = [category]
    elif matches == max_matches:
        suggested_categories.append(category)

for category in sorted(suggested_categories):
    print(category)