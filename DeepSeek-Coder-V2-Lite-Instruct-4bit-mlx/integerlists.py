def process_commands(commands, lst):
    reverse = False
    for command in commands:
        if command == 'R':
            reverse = not reverse
        elif command == 'D':
            if lst:
                if reverse:
                    lst.pop()  # Remove the last element for a reversed list
                else:
                    lst.pop(0)  # Remove the first element for a normal list
            else:
                return "error"
    if reverse:
        lst.reverse()
    return lst

def main():
    num_cases = int(input())
    results = []
    
    for _ in range(num_cases):
        commands = input()
        num_elements = int(input())
        lst_str = input()[1:-1].split(',')
        lst = list(map(int, lst_str)) if num_elements > 0 else []
        result = process_commands(commands, lst)
        results.append(result)
    
    for result in results:
        if result == "error":
            print(result)
        else:
            print('[' + ','.join(map(str, result)) + ']')

if __name__ == "__main__":
    main()