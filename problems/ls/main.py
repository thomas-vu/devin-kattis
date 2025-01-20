import re

def match_pattern(pattern, filename):
    pattern = pattern.replace('.', '\.').replace('*', '.*')
    regex = re.compile(pattern)
    return regex.match(filename) is not None

def main():
    pattern = input().strip()
    n = int(input().strip())
    files = [input().strip() for _ in range(n)]
    
    filtered_files = [file for file in files if match_pattern(pattern, file)]
    for file in filtered_files:
        print(file)

if __name__ == "__main__":
    main()