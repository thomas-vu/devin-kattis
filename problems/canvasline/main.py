def main():
    n = int(input())
    canvases = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    pegs = list(map(int, input().split()))
    
    # Create a list to store the positions of new pegs
    new_pegs = []
    
    # Iterate over each canvas to determine the positions of new pegs
    for left, right in canvases:
        # Check if there are already pegs at the required positions
        left_pegs = [peg for peg in pegs if left - 10 <= peg <= left]
        right_pegs = [peg for peg in pegs if right - 10 <= peg <= right]
        
        # If not exactly two pegs are available, place new ones
        if len(left_pegs) < 2:
            for peg in left_pegs:
                new_pegs.append(left - 1)
            for _ in range(2 - len(left_pegs)):
                new_pegs.append(left)
        if len(right_pegs) < 2:
            for peg in right_pegs:
                new_pegs.append(right)
            for _ in range(2 - len(right_pegs)):
                new_pegs.append(right)
    
    # If all canvases are secured with exactly two pegs, output the new pegs positions
    if all(left_pegs.count(peg) == 2 and right_pegs.count(peg) == 2 for left_pegs, right_pegs in zip(left_pegs, right_pegs)):
        print(len(new_pegs))
        for peg in new_pegs:
            print(peg, end=' ')
    else:
        print("impossible")

if __name__ == "__main__":
    main()