n = int(input())
meats = [input().strip() for _ in range(n)]

if "nautakjot" in meats and "kjuklingur" in meats:
    print("blandad best")
elif "nautakjot" in meats:
    print("nautakjot")
elif "kjuklingur" in meats:
    print("kjuklingur")