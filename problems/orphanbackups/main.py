def find_orphans(index, files):
    index_set = set(index)
    file_dict = {}
    
    for file in files:
        parts = file.split('_')
        image_name = parts[0]
        if image_name in index_set:
            file_dict.setdefault(image_name, []).append(file)
    
    orphans = [f for f in files if f.split('_')[0] not in index_set]
    orphan_files = [f for f in files if f.split('_')[0] not in index_set and 'INCR' in f]
    orphan_index = [i for i in index if i not in file_dict.keys()]
    
    return orphan_files, orphan_index

def main():
    index = []
    files = []
    
    while True:
        line = input()
        if not line:
            break
        index.append(line)
    
    while True:
        try:
            line = input()
            files.append(line)
        except EOFError:
            break
    
    orphan_files, orphan_index = find_orphans(index, files)
    
    if not orphan_files and not orphan_index:
        print("No mismatches.")
    else:
        for file in sorted(orphan_files):
            print(f"F {file}")
        for image in sorted(orphan_index):
            print(f"I {image}")

if __name__ == "__main__":
    main()