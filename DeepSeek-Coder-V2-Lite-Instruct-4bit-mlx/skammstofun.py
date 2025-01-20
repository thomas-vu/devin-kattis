n = int(input())
words = input().split()
abbreviation = ''.join([word[0] for word in words if word[0].isupper()])
print(abbreviation)