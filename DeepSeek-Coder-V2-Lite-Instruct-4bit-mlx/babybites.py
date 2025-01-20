def check_counting(n, bites):
    expected = 0
    for bite in bites:
        if bite == "mumble":
            expected += 1
        elif int(bite) == expected + 1:
            expected += 1
        else:
            return "something is fishy"
    return "makes sense"

n = int(input())
bites = input().split()
print(check_counting(n, bites))