def find_first_valid_word(dictionary, license_plate):
    for word in dictionary:
        if is_subsequence(license_plate, word):
            return word
    return "No valid word"

def is_subsequence(pattern, string):
    it = iter(string)
    return all(char in it for char in pattern)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    dictionary = data[2:N+2]
    license_plates = data[N+2:]
    
    results = []
    for plate in license_plates:
        result = find_first_valid_word(dictionary, plate)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()