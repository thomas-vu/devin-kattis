def find_cs_students(NCS, NES, iqs):
    mean_cs = sum(iqs[:NCS]) / NCS
    mean_ne = sum(iqs[NCS:]) / NES
    
    count = 0
    for i in range(NCS):
        new_mean_cs = (sum(iqs[:NCS]) - iqs[i] + sum(iqs[NCS:])) / (NCS - 1)
        if new_mean_cs > mean_cs and new_mean_cs == (sum(iqs[:NCS]) - iqs[i] + sum(iqs[NCS:])) / (NCS - 1):
            count += 1
    return count

def main():
    T = int(input())
    for _ in range(T):
        input()  # Consume the blank line
        NCS, NES = map(int, input().split())
        iqs = list(map(int, input().split()))
        result = find_cs_students(NCS, NES, iqs)
        print(result)

if __name__ == "__main__":
    main()