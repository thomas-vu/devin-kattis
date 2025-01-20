def find_common_substring(life_forms):
    def count_substrings(s1, s2):
        min_len = min(len(s1), len(s2))
        for i in range(min_len, 0, -1):
            if s1[:i] == s2[:i]:
                return i
        return 0

    n = len(life_forms)
    if n == 0:
        return "?"
    
    substrings = {}
    for form in life_forms:
        for i in range(len(form)):
            for j in range(i + 1, len(form) + 1):
                substring = form[i:j]
                if substring in substrings:
                    substrings[substring] += 1
                else:
                    substrings[substring] = 1
    
    common_substrings = []
    for substring, count in substrings.items():
        if count > n // 2:
            common_substrings.append(substring)
    
    if not common_substrings:
        return "?"
    
    common_substrings.sort()
    return common_substrings[0] if len(common_substrings) == 1 else common_substrings

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        life_forms = [input().strip() for _ in range(n)]
        result = find_common_substring(life_forms)
        
        if isinstance(result, list):
            for substring in result:
                print(substring)
        else:
            print(result)
        
        print()

if __name__ == "__main__":
    main()