def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        high, low = -1, 11
        honest = True
        while n != 'right on':
            if n == 'too high':
                high = min(high, int(n) - 1)
            elif n == 'too low':
                low = max(low, int(n) + 1)
            n = input()
        if not (low <= int(n) <= high):
            honest = False
        
        if honest:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")

main()