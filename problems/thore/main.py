def find_prefix(names):
    thore = "ThoreHusfeldt"
    for name in names:
        if name.startswith(thore):
            return "Thore is awesome"
    for i in range(1, len(thore)):
        prefix = thore[:i]
        if all(not name.startswith(prefix) for name in names if name != "ThoreHusfeldt"):
            return prefix
    return "Thore sucks"

n = int(input())
names = [input().strip() for _ in range(n)]
print(find_prefix(names))