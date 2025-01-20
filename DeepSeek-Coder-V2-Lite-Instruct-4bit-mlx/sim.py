def process_string(s):
    result = []
    cursor = 0
    
    for char in s:
        if char == '<':
            if cursor > 0:
                cursor -= 1
                result.pop(cursor)
        elif char == '[':
            cursor = 0
        elif char == ']':
            cursor = len(result)
        else:
            result.insert(cursor, char)
            cursor += 1
    
    return ''.join(result)

def main():
    T = int(input())
    for _ in range(T):
        s = input()
        print(process_string(s))

if __name__ == "__main__":
    main()