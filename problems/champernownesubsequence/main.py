n = int(input())
s = input()

def find_minimum_k(s):
    k = 1
    while True:
        word = ''.join(str(i) for i in range(1, k + 1))
        if all(char in word for char in s):
            return k
        k += 1

print(find_minimum_k(s))