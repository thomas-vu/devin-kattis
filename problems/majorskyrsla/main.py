def main():
    n, k = map(int, input().split())
    pages = list(range(1, n + 1))
    
    # Create a list to hold the index and page number pairs
    indexed_pages = [(i + 1, pages[i]) for i in range(n)]
    
    # Sort the indexed pages by page number (value) in descending order
    indexed_pages.sort(key=lambda x: -x[1])
    
    # Create a list to hold the final order of pages
    final_order = []
    
    # Iterate through the sorted indexed pages and add to the final order
    for idx, page in indexed_pages:
        if k == 0:
            break
        for j in range(idx):
            if indexed_pages[j][0] < idx and k > 0:
                final_order.append(indexed_pages[j][0])
                k -= 1
        final_order.append(idx)
    
    # Print the final order of pages
    print(' '.join(map(str, final_order)))

if __name__ == "__main__":
    main()