def calculate_pitas_and_pizzas(total_profit, pita_profit, pizza_profit):
    solutions = []
    for num_pitas in range(0, int(total_profit / pita_profit) + 1):
        remaining_profit = total_profit - num_pitas * pita_profit
        if remaining_profit % pizza_profit == 0:
            num_pizzas = int(remaining_profit / pizza_profit)
            solutions.append((num_pitas, num_pizzas))
    return solutions

def main():
    while True:
        try:
            pt, p1, p2 = map(float, input().split())
            solutions = calculate_pitas_and_pizzas(pt, p1, p2)
            if solutions:
                for solution in sorted(solutions):
                    print(f"{solution[0]} {solution[1]}")
            else:
                print("none")
        except EOFError:
            break

if __name__ == "__main__":
    main()