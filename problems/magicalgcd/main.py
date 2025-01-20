import math
from functools import reduce

def gcd_of_list(lst):
    x = reduce(math.gcd, lst)
    return gcd_of_list([x] + [y for y in lst if y != x])

def magical_gcd(lst):
    n = len(lst)
    max_magical_gcd = 0
    
    for i in range(n):
        current_gcd = lst[i]
        for j in range(i, n):
            current_gcd = math.gcd(current_gcd, lst[j])
            length = j - i + 1
            max_magical_gcd = max(max_magical_gcd, current_gcd * length)
    
    return max_magical_gcd

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        lst = list(map(int, input().split()))
        print(magical_gcd(lst))

if __name__ == "__main__":
    main()