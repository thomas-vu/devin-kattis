def main():
    N = int(input())
    balance = 0
    
    for _ in range(N):
        description = input()
        amount = int(input())
        balance += amount
    
    if balance > 0:
        print("Usch, vinst")
    elif balance < 0:
        print("Nekad")
    else:
        print("Lagom")

if __name__ == "__main__":
    main()