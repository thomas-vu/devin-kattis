def process_receipts(N, receipts):
    recorded = set()
    result = []
    
    for receipt in receipts:
        if receipt not in recorded:
            recorded.add(receipt)
            result.append(1)
        else:
            result.append(0)
    
    return result

# Main function to read input and print output
def main():
    N = int(input())
    receipts = list(map(int, input().split()))
    
    result = process_receipts(N, receipts)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()