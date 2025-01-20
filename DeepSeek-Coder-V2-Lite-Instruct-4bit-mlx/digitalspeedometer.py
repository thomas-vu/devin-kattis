import sys

tf = float(input())
tr = float(input())
speeds = []

while True:
    try:
        speed = float(input())
        if speed == 0:
            break
        speeds.append(speed)
    except EOFError:
        break

last_value = 0
for speed in speeds:
    if speed < 1:
        print(1)
    else:
        i = int(speed)
        j = i + 1
        if speed >= i and speed < i + tf:
            print(i)
        elif speed >= i + tr and speed < j:
            print(j)
        else:
            if last_value is not None and last_value < i + tr:
                print(j)
            else:
                print(i)
    last_value = speed