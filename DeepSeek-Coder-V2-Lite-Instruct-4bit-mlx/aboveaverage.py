def above_average(grades):
    average = sum(grades) / len(grades)
    above_count = sum(1 for grade in grades if grade > average)
    return (above_count / len(grades)) * 100

def main():
    C = int(input())
    for _ in range(C):
        N = list(map(int, input().split()))[0]
        grades = list(map(int, input().split()))
        percentage = above_average(grades)
        print("{:.3f}%".format(percentage))

if __name__ == "__main__":
    main()