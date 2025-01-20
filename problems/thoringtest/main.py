N = int(input())
words = [input().lower() for _ in range(N)]
sentence = input().lower().split()

contains_error = False
for word in sentence:
    if word not in words:
        contains_error = True
        break

if contains_error:
    print("Thore has left the chat")
else:
    print("Hi, how do I look today?")