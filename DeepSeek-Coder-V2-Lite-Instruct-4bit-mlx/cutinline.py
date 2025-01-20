def main():
    N = int(input())
    queue = [input() for _ in range(N)]
    C = int(input())
    
    for _ in range(C):
        event = input().split()
        if event[0] == 'cut':
            a, b = event[1], event[2]
            cut_position(queue, a, b)
        elif event[0] == 'leave':
            queue.remove(event[1])
    
    for person in queue:
        print(person)

def cut_position(queue, a, b):
    pos = queue.index(b)
    queue.insert(pos, a)

if __name__ == "__main__":
    main()