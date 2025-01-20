A, B = map(int, input().split())
remainder = A % B
if remainder == 0:
    print(0)
else:
    increase = B - remainder
    decrease = remainder
    print(min(increase, decrease))