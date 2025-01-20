def maximum_damage(a):
    xor_sum = 0
    spells = []
    for ai in a:
        xor_sum ^= ai
        spells.append(ai)
    return xor_sum, spells

def main():
    C = int(input())
    for _ in range(C):
        n = int(input())
        a = list(map(int, input().split()))
        max_damage, spells = maximum_damage(a)
        print(max_damage)
        for si in spells:
            print(si, end=' ')
        print()

if __name__ == "__main__":
    main()