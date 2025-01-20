def count_occurrences(S, L):
    def type1():
        return S.count(L)
    
    def type2():
        count = 0
        for i in range(len(S)):
            modified_S = S[:i] + S[i+1:]
            count += L.count(modified_S)
        return count
    
    def type3():
        unique_modifications = set()
        for i in range(len(S)):
            modified_S = S[:i] + S[i+1:]
            for j in range(len(S)):
                modified_S2 = S[:j] + S[j+1:]
                unique_modifications.add(modified_S2)
            for j in range(len(S)):
                modified_S = S[:i] + S[i+1:]
                for k in range(len(S)):
                    modified_S3 = S[:k] + S[k+1:]
                    unique_modifications.add(modified_S3)
        count = 0
        for modification in unique_modifications:
            count += L.count(modification)
        return count
    
    return type1(), type2(), type3()

while True:
    input_line = input().strip()
    if input_line == '0':
        break
    S, L = input_line.split()
    type1_count, type2_count, type3_count = count_occurrences(S, L)
    print(f"{type1_count} {type2_count} {type3_count}")