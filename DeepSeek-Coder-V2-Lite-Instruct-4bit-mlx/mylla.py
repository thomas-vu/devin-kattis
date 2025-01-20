def main():
    N = int(input())
    S = input()
    
    arnar_wins = 0
    hannes_wins = 0
    
    for char in S:
        if char == 'A':
            arnar_wins += 1
        else:
            hannes_wins += 1
    
    if arnar_wins > hannes_wins:
        print("Arnar")
    else:
        print("Hannes")

if __name__ == "__main__":
    main()