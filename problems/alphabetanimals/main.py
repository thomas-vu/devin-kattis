def can_eliminate(last, unused):
    for name in unused:
        if name.startswith(last[-1]):
            return True, name
    return False, None

def main():
    last = input().strip()
    n = int(input().strip())
    unused = [input().strip() for _ in range(n)]
    
    can_eliminate_next, name = can_eliminate(last, unused)
    
    if can_eliminate_next:
        print(f"{name}!")
    elif unused:
        print(unused[0])
    else:
        print("?")

if __name__ == "__main__":
    main()