import sys

def main():
    N = int(sys.stdin.readline().strip())
    total_seconds = 0
    total_minutes = 0
    
    for _ in range(N):
        M, S = map(int, sys.stdin.readline().strip().split())
        total_seconds += S
        total_minutes += M
    
    average_length = total_seconds / (total_minutes * 60)
    
    if average_length > 1:
        print("{:.7f}".format(average_length))
    else:
        print("measurement error")

if __name__ == "__main__":
    main()