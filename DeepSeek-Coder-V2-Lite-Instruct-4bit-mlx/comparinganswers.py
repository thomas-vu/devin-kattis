import sys

def read_ints():
    return list(map(int, input().split()))

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        adj_matrix = [read_ints() for _ in range(n)]
        friend_answers = [read_ints() for _ in range(n)]
        
        calculated_matrix = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if adj_matrix[i][j] != 0:
                    for k in range(n):
                        if adj_matrix[j][k] != 0:
                            calculated_matrix[i][k] += adj_matrix[i][j] * adj_matrix[j][k]
        
        correct = True
        for i in range(n):
            for j in range(n):
                if calculated_matrix[i][j] != friend_answers[i][j]:
                    correct = False
                    break
            if not correct:
                break
        
        print("YES" if correct else "NO")

if __name__ == "__main__":
    main()