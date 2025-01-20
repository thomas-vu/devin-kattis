def can_jim_complete_adventure(adventure):
    stack = []
    for item in adventure:
        if item in '$.b.|*tj':
            stack.append(item)
        elif item == '.':
            continue
        else:
            if stack and ((item == 'b' and stack[-1] == '$') or 
                          (item == 't' and stack[-1] == '*') or 
                          (item == 'j' and stack[-1] == '|')):
                stack.pop()
            else:
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"

def main():
    n = int(input())
    for _ in range(n):
        adventure = input()
        result = can_jim_complete_adventure(adventure)
        print(result)

if __name__ == "__main__":
    main()