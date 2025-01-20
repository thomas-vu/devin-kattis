def main():
    journey = input()
    money, gold, jewels = 0, 0, 0
    stack = []
    
    for item in journey:
        if item == 'p':
            stack.append('p')
        elif item == 'g':
            stack.append('g')
        elif item == 'o':
            stack.append('o')
        elif item == 'P':
            if stack and stack[-1] == 'p':
                money += 1
                stack.pop()
            else:
                print("Neibb")
                return
        elif item == 'G':
            if stack and stack[-1] == 'g':
                gold += 1
                stack.pop()
            else:
                print("Neibb")
                return
        elif item == 'O':
            if stack and stack[-1] == 'o':
                jewels += 1
                stack.pop()
            else:
                print("Neibb")
                return
        elif item == '.':
            continue
    
    print(money)
    print(gold)
    print(jewels)

main()