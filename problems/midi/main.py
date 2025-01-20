n = int(input())
notes = [input() for _ in range(n)]
original_message = ""
for i in reversed(range(n)):
    original_message += notes[i]
print(original_message)