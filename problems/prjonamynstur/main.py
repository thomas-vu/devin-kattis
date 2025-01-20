def calculate_yarn_cost(recipe):
    yarn_cost = 0
    for row in recipe:
        for symbol in row:
            yarn_cost += get_yarn_for_symbol(symbol)
    return yarn_cost

def get_yarn_for_symbol(symbol):
    if symbol == '.':
        return 5
    elif symbol == 'O':
        return 10
    elif symbol == 'A':
        return 25
    elif symbol == '/':
        return 25
    elif symbol == '\\':
        return 25
    elif symbol == 'v':
        return 22
    elif symbol == '^':
        return 20
    else:
        return 0

def main():
    n, m = map(int, input().split())
    recipe = [input() for _ in range(n)]
    total_yarn = calculate_yarn_cost(recipe)
    print(total_yarn)

if __name__ == "__main__":
    main()