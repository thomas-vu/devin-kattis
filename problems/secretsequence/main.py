n = int(input())
a, b, c, d = 0, 1, n-1, n
print("? {} {} {} {}".format(a, b, c, d))
response = int(input())
if response == 1:
    ones_count = n
elif response == -1:
    ones_count = 0
else:
    print("? {} {} {} {}".format(a, b+1, c-1, d))
    response2 = int(input())
    if response2 == 0:
        ones_count = b - a + c - d + (1 if response == 0 else 0)
    elif response2 == 1:
        ones_count = b - a + (n - c)
    else:
        ones_count = n - d
print("! {}".format(ones_count))