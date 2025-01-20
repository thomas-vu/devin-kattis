def base62_to_int(s):
    num = 0
    for char in s:
        if '0' <= char <= '9':
            num = num * 62 + int(char)
        elif 'a' <= char <= 'z':
            num = num * 62 + ord(char) - ord('a') + 10
        elif 'A' <= char <= 'Z':
            num = num * 62 + ord(char) - ord('A') + 36
    return num

def compare_base62(s1, s2):
    int1 = base62_to_int(s1)
    int2 = base62_to_int(s2)
    return int1 < int2

t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    if compare_base62(s1, s2):
        print("YES")
    else:
        print("NO")