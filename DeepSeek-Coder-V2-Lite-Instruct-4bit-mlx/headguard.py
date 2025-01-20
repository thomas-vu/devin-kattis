def process_string(s):
    result = ""
    count = 1
    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            result += str(count) + s[i]
            count = 1
    return result

def main():
    import sys
    input_lines = sys.stdin.read().splitlines()
    for line in input_lines:
        print(process_string(line))

if __name__ == "__main__":
    main()