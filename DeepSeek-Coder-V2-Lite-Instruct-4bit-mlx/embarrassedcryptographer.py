def find_smallest_factor(k, l):
    for i in range(2, int(l**0.5) + 1):
        if k % i == 0:
            return str(i)
    return "GOOD"

while True:
    k, l = map(int, input().split())
    if k == 0 and l == 0:
        break
    result = find_smallest_factor(k, l)
    if result == "GOOD":
        print("GOOD")
    else:
        print(f"BAD {result}")