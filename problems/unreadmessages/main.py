def main():
    n, m = map(int, input().split())
    senders = [0] * (n + 1)
    unread_count = [0] * (n + 1)
    
    for _ in range(m):
        s = int(input())
        senders[s] += 1
        unread_count[s] = sum(senders) - senders[s]
        print(sum(unread_count))

if __name__ == "__main__":
    main()