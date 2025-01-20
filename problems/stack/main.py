def min_operations_to_print(s):
    operations = 0
    stack = []
    
    for char in s:
        if not stack or stack[-1] != char:
            stack.append(char)
            operations += 1
        else:
            stack.pop()
            operations += 1
    
    while stack:
        stack.pop()
        operations += 1
    
    return operations

def main():
    T = int(input())
    for _ in range(T):
        s = input()
        print(min_operations_to_print(s))

if __name__ == "__main__":
    main()