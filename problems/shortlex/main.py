def find_binary_string(i):
    if i == 1:
        return "0"
    elif i == 2:
        return "1"
    
    index = 3
    length = 2
    while index <= i:
        next_index = index + (1 << length)
        if next_index > i:
            break
        index = next_index
        length += 1
    
    result = []
    while i >= 3:
        if i < index:
            result.append("0")
            index -= (1 << length) - 1
        else:
            result.append("1")
            i -= index
        length -= 1
    
    while len(result) < length:
        result.append("0")
    
    return "".join(reversed(result))

def main():
    T = int(input())
    for _ in range(T):
        i = int(input())
        print(find_binary_string(i))

if __name__ == "__main__":
    main()