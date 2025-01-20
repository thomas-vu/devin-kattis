def median_of_three(a, b, c):
    if (a > b and a < c) or (a < b and a > c):
        return a
    elif (b > a and b < c) or (b < a and b > c):
        return b
    else:
        return c

def process_action(N, t, A):
    if t == 1:
        print("7")
    elif t == 2:
        if A[0] > A[1]:
            print("Bigger")
        elif A[0] == A[1]:
            print("Equal")
        else:
            print("Smaller")
    elif t == 3:
        print(median_of_three(A[0], A[1], A[2]))
    elif t == 4:
        print(sum(A))
    elif t == 5:
        even_sum = sum([a for a in A if a % 2 == 0])
        print(even_sum)
    elif t == 6:
        result = ""
        for a in A:
            index = a % 26
            result += chr(ord('a') + index)
        print(result)
    elif t == 7:
        visited = set()
        while True:
            if A[i] < 0 or A[i] >= N:
                print("Out")
                break
            elif A[i] == N - 1:
                print("Done")
                break
            elif A[i] in visited:
                print("Cyclic")
                break
            else:
                visited.add(A[i])
                i = A[i]

# Read input
N, t = map(int, input().split())
A = list(map(int, input().split()))

# Process the action based on t
process_action(N, t, A)