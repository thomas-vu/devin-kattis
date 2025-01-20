def distribute_funding(n):
    departments = []
    money_left = n
    i = 1
    while money_left > 0:
        if money_left >= i and (i == 1 or departments[-1] != i - 1):
            departments.append(i)
            money_left -= i
        else:
            break
        i += 1
    return departments

n = int(input())
departments = distribute_funding(n)
print(len(departments))
print(" ".join(map(str, departments)))