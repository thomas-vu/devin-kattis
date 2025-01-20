def main():
    N, M = map(int, input().split())
    friends = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
    
    instruments = [''] * (N + 1)
    for i in range(1, N + 1):
        if instruments[i] == '':
            # Try both instruments for student i
            instruments[i] = 'P'
            stack = [i]
            while stack:
                student = stack.pop()
                for friend in friends[student]:
                    if instruments[friend] == '':
                        # Assign the opposite instrument to friend
                        instruments[friend] = 'S' if instruments[student] == 'P' else 'P'
                        stack.append(friend)
                    elif instruments[friend] == instruments[student]:
                        # Conflict, backtrack
                        instruments = [''] * (N + 1)
                        break
                if instruments[student] == '':
                    # Backtrack by resetting the instrument for student i
                    instruments[i] = ''
                    break
    
    print(''.join(instruments[1:]))

if __name__ == "__main__":
    main()