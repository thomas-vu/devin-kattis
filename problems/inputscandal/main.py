# Read input until EOF
lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

# Output the number of lines and the lines themselves
print(len(lines))
for line in lines:
    print(line)