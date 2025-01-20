def find_longest_substring(A, B):
    def is_permutation(s1, s2):
        return sorted(s1) == sorted(s2)
    
    n = len(A)
    max_len = 0
    start_idx = -1
    
    for i in range(n):
        for j in range(i, n):
            sub_A = A[i:j+1]
            for k in range(n - len(sub_A) + 1):
                sub_B = B[k:k+len(sub_A)]
                if is_permutation(sub_A, sub_B):
                    if len(sub_A) > max_len:
                        max_len = len(sub_A)
                        start_idx = i
                    elif len(sub_A) == max_len and i < start_idx:
                        start_idx = i
    
    if max_len == 0:
        return "NONE"
    else:
        return A[start_idx:start_idx+max_len]

def main():
    n = int(input())
    for _ in range(n):
        A = input()
        B = input()
        result = find_longest_substring(A, B)
        print(result)

if __name__ == "__main__":
    main()