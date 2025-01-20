import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def majority_card(N, rounds):
    deck = deque()
    
    for round in rounds:
        command, *args = round.split()
        
        if command == "PUT_TOP":
            X, Y = map(int, args)
            for _ in range(X):
                deck.appendleft(Y)
        elif command == "PUT_BOTTOM":
            X, Y = map(int, args)
            for _ in range(X):
                deck.append(Y)
        elif command == "REMOVE_TOP":
            Z = int(args[0])
            for _ in range(Z):
                if deck:
                    deck.popleft()
        elif command == "REMOVE_BOTTOM":
            Z = int(args[0])
            for _ in range(Z):
                if deck:
                    deck.pop()
        
        count = defaultdict(int)
        for card in deck:
            count[card] += 1
        
        max_count = max(count.values(), default=0)
        majority_cards = [card for card, cnt in count.items() if cnt == max_count]
        print(min(majority_cards))

# Read input
N = int(input())
rounds = [input().strip() for _ in range(N)]

# Process the rounds and find the majority card
majority_card(N, rounds)