def main():
    n, c, s, f = map(int, input().split())
    sigma = input()
    final_states = set(map(int, input().split()))
    transitions = [list(map(int, input().split())) for _ in range(n)]
    
    m = int(input())
    strings = [input() for _ in range(m)]
    
    for string in strings:
        state = s
        accepted = False
        for char in string:
            index = sigma.index(char)
            state = transitions[state - 1][index]
        if state in final_states:
            accepted = True
        print("accept" if accepted else "reject")

if __name__ == "__main__":
    main()