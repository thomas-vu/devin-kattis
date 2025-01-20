def preprocess(keyword):
    return keyword.replace('-', ' ').lower()

def main():
    n = int(input())
    keywords = set()
    
    for _ in range(n):
        keyword = input().strip()
        normalized_keyword = preprocess(keyword)
        keywords.add(normalized_keyword)
    
    unique_keywords = set()
    for keyword in keywords:
        if keyword not in unique_keywords:
            unique_keywords.add(keyword)
    
    print(len(unique_keywords))

if __name__ == "__main__":
    main()