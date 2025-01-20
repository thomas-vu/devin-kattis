def main():
    S = input().strip()
    suits = {'P': set(), 'K': set(), 'H': set(), 'T': set()}
    n = len(S) // 3
    
    for i in range(n):
        card = S[i*3:(i+1)*3]
        suit, num = card[:1], card[1:]
        
        if card in suits[suit]:
            print("GRESKA")
            return
        
        suits[suit].add(card)
    
    missing = {suit: 13 - len(cards) for suit, cards in suits.items()}
    print(f"{missing['P']} {missing['K']} {missing['H']} {missing['T']}")

if __name__ == "__main__":
    main()