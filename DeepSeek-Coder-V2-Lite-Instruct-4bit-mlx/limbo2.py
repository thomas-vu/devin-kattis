def find_building_block(R, C):
    size = 1
    level = 0
    
    while True:
        if R >= size and C < size:
            break
        if R < size and C >= size:
            break
        size *= 2
        level += 1
    
    block_number = 0
    while level > 0:
        if R >= size and C < size:
            block_number += (size // 2) * (size // 2)
            C -= size // 2
        elif R < size and C >= size:
            block_number += (size // 2) * (size // 2) * 3
            R -= size // 2
        else:
            block_number += (size // 2) * (size // 2) * 2
            R -= size // 2
            C -= size // 2
        size *= 2
        level -= 1
    
    if R < size and C < size:
        block_number += R * (size // 2) + C + 1
    
    return block_number

def main():
    T = int(input())
    results = []
    for _ in range(T):
        R, C = map(int, input().split())
        results.append(find_building_block(R, C))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()