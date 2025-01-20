def read_input():
    n, b = map(int, input().split())
    troops = [tuple(map(float, input().split())) for _ in range(n)]
    return n, b, troops

def calculate_efficacy(troops, budget):
    max_efficacy = 0.0
    for mask in range(1, 1 << len(troops)):
        cost = 0.0
        health = 0.0
        potency = 0.0
        for i in range(len(troops)):
            if mask & (1 << i):
                c, h, p = troops[i]
                cost += c
                health += c * h
                potency += c * p
        if cost <= budget:
            max_efficacy = max(max_efficacy, health * potency)
    return max_efficacy

def main():
    n, b, troops = read_input()
    max_efficacy = calculate_efficacy(troops, b)
    print("{:.2f}".format(max_efficacy))

if __name__ == "__main__":
    main()