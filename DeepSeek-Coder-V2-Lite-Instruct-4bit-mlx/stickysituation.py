def can_form_triangle(sticks):
    sticks.sort()
    for i in range(2, len(sticks)):
        if sticks[i-2] + sticks[i-1] > sticks[i]:
            return "possible"
    return "impossible"

N = int(input())
sticks = list(map(int, input().split()))
print(can_form_triangle(sticks))