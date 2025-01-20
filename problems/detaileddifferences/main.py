def compare_strings(str1, str2):
    result = ""
    for char1, char2 in zip(str1, str2):
        if char1 == char2:
            result += "."
        else:
            result += "*"
    return result

def main():
    n = int(input())
    for _ in range(n):
        str1 = input()
        str2 = input()
        comparison = compare_strings(str1, str2)
        print(str1)
        print(str2)
        print(comparison)
        if _ < n - 1:
            print()

if __name__ == "__main__":
    main()