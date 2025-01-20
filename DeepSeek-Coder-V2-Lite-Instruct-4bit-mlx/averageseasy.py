def find_cs_students(NCS, NES, iqs):
    cs_iqs = iqs[:NCS]
    econ_iqs = iqs[NCS:]
    
    cs_sum = sum(cs_iqs)
    econ_sum = sum(econ_iqs)
    
    avg_cs_before = cs_sum / NCS
    avg_econ_before = econ_sum / NES
    
    count = 0
    for i in range(NCS):
        temp_cs_sum = cs_sum - cs_iqs[i]
        new_avg_cs = (temp_cs_sum) / (NCS - 1)
        new_avg_econ = econ_sum / NES
        
        if new_avg_cs < new_avg_econ:
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