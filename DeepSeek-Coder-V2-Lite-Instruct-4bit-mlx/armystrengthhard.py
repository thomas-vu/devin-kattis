def determine_winner(godzilla, mechagodzilla):
    if not godzilla:
        return "MechaGodzilla"
    if not mechagodzilla:
        return "Godzilla"
    if min(godzilla) < min(mechagodzilla):
        return "Godzilla"
    elif min(godzilla) > min(mechagodzilla):
        return "MechaGodzilla"
    else:
        return "uncertain"

def main():
    T = int(input())
    for _ in range(T):
        input()  # Consume the blank line
        NG = int(input())
        Godzilla_army = list(map(int, input().split()))
        NM = int(input())
        MechaGodzilla_army = list(map(int, input().split()))
        
        winner = determine_winner(Godzilla_army, MechaGodzilla_army)
        print(winner)

if __name__ == "__main__":
    main()