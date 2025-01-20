def main():
    N = int(input())
    slats = []
    
    for _ in range(N):
        sword_slats = input().strip()
        slats.append([int(x) for x in sword_slats])
    
    top = 0
    bottom = 0
    left = 0
    right = 0
    
    for sword in slats:
        if sword[0] == 1:
            continue
        elif sword[0] == 0:
            top += 1
        if sword[1] == 1:
            continue
        elif sword[1] == 0:
            bottom += 1
        if sword[2] == 1:
            continue
        elif sword[2] == 0:
            left += 1
        if sword[3] == 1:
            continue
        elif sword[3] == 0:
            right += 1
    
    swords_made = min(top // 2, bottom // 2, left // 2, right // 2)
    remaining_top = top - swords_made * 2
    remaining_bottom = bottom - swords_made * 2
    remaining_left = left - swords_made * 2
    remaining_right = right - swords_made * 2
    
    print(swords_made, remaining_top + remaining_bottom, remaining_left + remaining_right)

main()