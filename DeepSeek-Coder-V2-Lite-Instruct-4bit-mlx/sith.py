# Read input from the user
name = input()
a = int(input())
b = int(input())
result = int(input())

# Determine the force user's allegiance based on the given rules
if abs(a - b) == result:
    print("SITH")
elif a - b == result:
    print("JEDI")
else:
    print("VEIT EKKI")