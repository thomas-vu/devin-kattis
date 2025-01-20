a, b, c = map(int, input().split())
if a**(b**c) == (a**b)**c:
    print("What an excellent example!")
else:
    print("Oh look, a squirrel!")