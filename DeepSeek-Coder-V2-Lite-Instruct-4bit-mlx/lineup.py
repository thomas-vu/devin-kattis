def check_order(names):
    if all(names[i] <= names[i + 1] for i in range(len(names) - 1)):
        return "INCREASING"
    elif all(names[i] >= names[i + 1] for i in range(len(names) - 1)):
        return "DECREASING"
    else:
        return "NEITHER"

def main():
    N = int(input())
    names = [input().strip() for _ in range(N)]
    result = check_order(names)
    print(result)

if __name__ == "__main__":
    main()