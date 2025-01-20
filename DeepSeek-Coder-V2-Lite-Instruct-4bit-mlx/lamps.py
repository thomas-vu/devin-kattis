def cost_incandescent(h, days):
    return (5 * 2 / 1000 + h * days * 60 / 100000) * (days // 1000 + (1 if days % 1000 else 0))

def cost_low_energy(h, days):
    return (60 / 8000 + h * days * 11 / 100000) * (days // 8000 + (1 if days % 8000 else 0))

def main():
    h, P = map(int, input().split())
    days = 0
    while cost_low_energy(h, days) >= cost_incandescent(h, days):
        days += 1
    print(days)

if __name__ == "__main__":
    main()