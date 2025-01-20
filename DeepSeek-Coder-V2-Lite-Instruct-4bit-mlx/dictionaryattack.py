def is_acceptable(password, dictionary):
    def count_changes(word1, word2):
        changes = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                changes += 1
        return changes

    for word in dictionary:
        if count_changes(password, word) <= 3:
            return True
    return False

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    dictionary = data[1:N+1]
    candidates = data[N+1:]
    
    acceptable_passwords = [password for password in candidates if is_acceptable(password, dictionary)]
    
    for password in acceptable_passwords:
        print(password)

if __name__ == "__main__":
    main()