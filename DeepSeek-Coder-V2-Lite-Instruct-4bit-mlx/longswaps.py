def can_sort_string(s, k):
    if len(set(s)) == 1:
        return "Yes"
    
    for i in range(len(s)):
        for j in range(i + k, len(s)):
            if s[i] > s[j]:
                s = list(s)
                s[i], s[j] = s[j], s[i]
                break
        else:
            return "No"
    return "Yes"

def main():
    s, k = input().split()
    k = int(k)
    result = can_sort_string(s, k)
    print(result)

if __name__ == "__main__":
    main()