def find_most_fun_gift(gifts):
    max_fun = -1
    most_fun_guest = ""
    for gift in gifts:
        name, fun_value = gift.split()
        fun_value = int(fun_value)
        if fun_value > max_fun:
            max_fun = fun_value
            most_fun_guest = name
    return most_fun_guest

n = int(input())
gifts = [input() for _ in range(n)]
most_fun_gift = find_most_fun_gift(gifts)
print(most_fun_gift)